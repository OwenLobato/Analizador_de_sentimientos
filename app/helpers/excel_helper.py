""" EXCEL helper module """

import pandas as pd
import dateutil.parser
from flask import flash
from textblob import TextBlob
from googletrans import Translator
from models.page_model import Page
from models.post_model import Post
from models.file_model import File
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
                'react_angry',
                'react_haha',
                'react_like',
                'react_love',
                'react_sad',
                'react_wow',
                'react_care',
                'share'
            ]
        )
        return excel_posts

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

    def __save_posts(self, restaurant_id, file_id):
        """ Save excel posts in db """
        excel_posts = self.read_posts()
        for index, row in excel_posts.iterrows():
            try:
                page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
                post_id = str(row['post_id'])
                file_fetch = File().find_by_params({'id': file_id})
                created_date = dateutil.parser.parse(str(row['created_date'])).date()
                created_time = row['created_time']
                message = str(row['message'])
                classification = str(row['classification'])
                xformat = str(row['format'])
                share = int(row['share'])
                react_angry = int(row['react_angry'])
                react_haha = int(row['react_haha'])
                react_like = int(row['react_like'])
                react_love = int(row['react_love'])
                react_sad = int(row['react_sad'])
                react_wow = int(row['react_wow'])
                react_care = int(row['react_care'])
                post_reactions = {
                    "angry": react_angry,
                    "haha": react_haha,
                    "like": react_like,
                    "love": react_love,
                    "sad": react_sad,
                    "wow": react_wow,
                    "care": react_care
                }
                reaction = self.__get_post_reaction(post_reactions)
                if not page_fetch:
                    return flash('Favor de previamente registrar una pagina','error')
                params = {
                    "id": post_id,
                    "file_id": file_fetch.id,
                    "created_time": created_time,
                    "created_date": created_date,
                    "message": message,
                    "classification": classification,
                    "xformat": xformat,
                    "share": share,
                    "angry": react_angry,
                    "haha": react_haha,
                    "like": react_like,
                    "love": react_love,
                    "sad": react_sad,
                    "wow": react_wow,
                    "care": react_care,
                    "reaction": reaction
                }
                post = Post(**params)
                post.create()
            except ValueError as e:
                error = 'Error en formato:', e
                return flash(error, 'error')
            except:
                return flash('Limpie y ponga en formato su archivo para publicaciones', 'error')
        return True

    def __get_post_reaction(self, post_reactions):
        """Get the post reaction by max reaction

        Args:
            post_reactions (dict): Total amount of each of the 7 facebook reactions
                                    (angry, haha, like, love, sad, wow, care)

        Returns:
            String: The reaction of the publication according to the one with the most quantity
        """
        total_reactions = (
            post_reactions['angry'] +
            post_reactions['haha'] +
            post_reactions['like'] +
            post_reactions['love'] +
            post_reactions['sad'] +
            post_reactions['wow'] +
            post_reactions['care']
        )
        if total_reactions != 0:
            val_max = max(post_reactions, key = post_reactions.get)
            if val_max == 'angry':
                post_react = 'Disgustante'
            if val_max == 'haha':
                post_react = 'Divertida'
            if val_max == 'like':
                post_react = 'Llamativa'
            if val_max == 'love':
                post_react = 'Encantadora'
            if val_max == 'sad':
                post_react = 'Triste'
            if val_max == 'wow':
                post_react = 'Impresionante'
            if val_max == 'care':
                post_react = 'Relevante'
        else:
            post_react = 'Aburrida'
        return post_react

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
                feeling = self.__get_message_sentiment(message)
                params = {
                    "post_id": post_id,
                    "from_name": from_name,
                    "gender": gender,
                    "created_time": created_time,
                    "created_date": created_date,
                    "message": message,
                    "feeling": feeling,
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

    def __get_message_sentiment(self, comment):
        """ Translate and make sentiment analysis to a comment

        Args:
            comment (String): Spanish comment

        Returns:
            String: Feeling of the comment
        """
        translator = Translator()
        trans_text = translator.translate(comment, dest='en')
        text = TextBlob(trans_text.text)
        polarity = text.sentiment.polarity
        feeling = 'Neutro'
        if polarity > 0:
            feeling = 'Positivo'
        elif polarity < 0:
            feeling = 'Negativo'
        return feeling

    def save_excel_data(self, restaurant_id, file_id):
        posts_db = self.__save_posts(restaurant_id, file_id)
        comments_db = self.__save_comments()
        if posts_db and comments_db:
            return True
        return False

    def delete_excel_data(self, restaurant_id, file_id):
        page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
        posts_fetch = Post().get_all({'file_id': file_id})
        if page_fetch and posts_fetch:
            for post in posts_fetch:
                Comment().destroy(post.id)
            Post().destroy(file_id)

    @staticmethod
    def read_db_file(file_id):
        """ Read db excel file by id

        Args:
            file_id (int): Id of the excel file

        Returns:
            file_fetch (File obj): File object by id
            posts_fetch (List): POSTS objects
            comments_fetch (Dict): COMMENTS objects, (Key: post_id - Value: Comment)
        """
        file_fetch = File().find_by_params({'id': file_id})
        posts_fetch = Post().get_all({'file_id': file_id}, True)
        comments_fetch = {}
        for post in posts_fetch:
            all_comments = Comment().get_all({'post_id': post.id})
            comments_fetch[post.id] = all_comments if all_comments else ['Sin comentarios']
        return (file_fetch, posts_fetch, comments_fetch)
