
from django.urls import resolve
from django.test import TestCase
from django.test import SimpleTestCase

from posts.models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="FirstSentense")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_object_name = f'{post.text}'
        assert excepted_object_name == 'FirstSentense'


class HomePageTest(TestCase):

    def setUp(self):
        Post.objects.create(text='qqq')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        assert resp.status.code == 200

    def test_view_yrl_by_name(self):
        resp = self.client.get(reverse('home'))
        assert resp.status.code == 200

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        assert resp.status.code == 200
        self.assertTemplateUsed(resp, 'home.html')



    # def test_uses_home_template(self):
    #     response = self.client.get('/home/')
    #     self.assertTemplateUsed(response, 'home/home.html')
    #



# def test_title(browser):
#
#     browser.get('http://127.0.0.1:8000/home/')
#     header_text = browser.find_element_by_tag_name('h1').text
#
#     # inputbox = browser.find_element_by_id('new_item_ID')
#     # inputbox.send_keys('HHHhhh')
#
#     assert header_text == 'Server_hh'
#     assert browser.title == 'Server4'
#
#
#
#
# class SimpleTests(SimpleTestCase):
#
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         assert response.status_code == 200
#
#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         assert response.status_code == 200


# def test_home_visit():
#     found = resolve('/home/')
#     assert found.func == home_visit
#
