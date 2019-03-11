from django.test import TestCase

# Create your tests here.

import datetime
from .models import Question

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


def create_question(question_text, days):
    """
    Create a question with the given 'question_test" and publish the given
    numbewr of 'days' to now (negative for questions published in the past,
    positive for questions yet to be published.
    :param days:
    :return:
    """

    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTest(TestCase):
    """was_published_recently() returns false for questions published in the future"""

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """
        if no questions exist, an appropriate message is displayed.
        :return:
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


    def test_past_question(self):
        """

        :return:
        """
        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )


    def test_future_question(self):
        """
        questions with a pub_date in the future aren't displayed on the index page.
        :return:
        """
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )


    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only displays
        past questions.
        :return:
        """
        create_question(question_text='Past question.', days=-30)
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )


    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions
        :return:
        """
        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
