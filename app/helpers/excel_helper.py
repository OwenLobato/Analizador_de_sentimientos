""" EXCEL helper module """

import pandas as pd
import dateutil.parser
from flask import flash
from models.page_model import Page
from models.post_model import Post
from models.reaction_model import Reaction
from models.comment_model import Comment

# pylint: disable=C0103

class ExcelHelper():
    """ Excel helper """

    def __init__(self, path):
        self.file_path = path

    def read_posts(self):
        """ Read the excel posts """
        excel_posts = pd.read_excel(
            self.file_path,
            sheet_name=0,
            skiprows=1,
            usecols=[
                'created_date',
                'created_time',
                'message',
                'classification',
                'format',
                'post_id',
                'share'
            ]
        )
        return excel_posts

    def read_reactions(self):
        """ Read the excel post reactions """
        excel_posts_reactions = pd.read_excel(
            self.file_path,
            sheet_name=0,
            skiprows=1,
            usecols=[
                'post_id',
                'react_angry',
                'react_haha',
                'react_like',
                'react_love',
                'react_sad',
                'react_wow',
                'react_care'
            ]
        )
        return excel_posts_reactions

    def read_comments(self):
        """ Read the excel comments """
        excel_comments = pd.read_excel(
            self.file_path,
            sheet_name=1,
            skiprows=1,
            usecols=[
                'post_id',
                'created_date',
                'created_time',
                'from_name',
                'message',
                'gender',
                'reactions'
            ]
        )
        return excel_comments

    def __save_posts(self, restaurant_id):
        """ Save excel posts in db """
        excel_posts = self.read_posts()
        for index, row in excel_posts.iterrows():
            try:
                created_date = dateutil.parser.parse(str(row['created_date'])).date()
                created_time = row['created_time']
                message = str(row['message'])
                classification = str(row['classification'])
                xformat = str(row['format'])
                post_id = str(row['post_id'])
                share = int(row['share'])
                page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
                if not page_fetch:
                    return flash('Favor de previamente registrar una pagina','error')
                params = {
                    "id": post_id,
                    "page_id": page_fetch.id,
                    "created_time": created_time,
                    "created_date": created_date,
                    "message": message,
                    "classification": classification,
                    "xformat": xformat,
                    "share": share
                }
                post = Post(**params)
                post.create()
            except ValueError as e:
                error = 'Error en formato:', e
                return flash(error, 'error')
            except:
                return flash('Limpie y ponga en formato su archivo para publicaciones', 'error')
        return True

    def __save_reactions(self):
        """ Save excel post reactions in db """
        excel_posts_reactions = self.read_reactions()
        for index, row in excel_posts_reactions.iterrows():
            try:
                post_id = str(row['post_id'])
                post_fetch = Post().find_by_params({'id': post_id})
                if not post_fetch:
                    continue
                react_angry = int(row['react_angry'])
                react_haha = int(row['react_haha'])
                react_like = int(row['react_like'])
                react_love = int(row['react_love'])
                react_sad = int(row['react_sad'])
                react_wow = int(row['react_wow'])
                react_care = int(row['react_care'])
                params = {
                    "post_id": post_id,
                    "angry": react_angry,
                    "haha": react_haha,
                    "like": react_like,
                    "love": react_love,
                    "sad": react_sad,
                    "wow": react_wow,
                    "care": react_care
                }
                reaction = Reaction(**params)
                reaction.create()
            except ValueError as e:
                error = 'Error en formato:', e
                return flash(error, 'error')
            except:
                return flash('Limpie y ponga en formato su archivo para las reacciones', 'error')
        return True

    def __save_comments(self):
        """ Save excel vcomments in db """
        excel_comments = self.read_comments()
        for index, row in excel_comments.iterrows():
            try:
                post_id = str(row['post_id'])
                post_fetch = Post().find_by_params({'id': post_id})
                if not post_fetch:
                    continue
                created_date =  dateutil.parser.parse(str(row['created_date'])).date()
                created_time = row['created_time']
                from_name = str(row['from_name'])
                message = str(row['message'])
                gender = str(row['gender'])[0]
                reactions = int(row['reactions'])
                params = {
                    "post_id": post_id,
                    "from_name": from_name,
                    "gender": gender,
                    "created_time": created_time,
                    "created_date": created_date,
                    "message": message,
                    "reactions": reactions
                }
                comments = Comment(**params)
                comments.create()
            except ValueError as e:
                error = 'Error en formato:', e
                return flash(error, 'error')
            except Exception as e:
                return flash('Limpie y ponga en formato su archivo para los comentarios', 'error')
        return True

    def save_excel_data(self, restaurant_id):
        posts_db = self.__save_posts(restaurant_id)
        reactions_db = self.__save_reactions()
        comments_db = self.__save_comments()
        if posts_db and reactions_db and comments_db:
            return True
        return False


    def delete_excel_data(self, restaurant_id):
        page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
        posts_fetch = Post().get_all({'page_id': page_fetch.id})
        if page_fetch and posts_fetch:
            for post in posts_fetch:
                Comment().destroy(post.id)
                Reaction().destroy(post.id)
            Post().destroy(page_fetch.id)
