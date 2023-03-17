from django.test import TestCase

from ..models import Group, Post, User, Comment


class TestData(TestCase):
    """Creat test data."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост более 15 символов',
        )
        cls.comment_post = Comment.objects.create(
            author=cls.user,
            text='Мой первый комментарий',
            post=cls.post,
        )

    class Meta:
        abstract = True


class PostModelTest(TestData):
    """Post model testing"""
    def test_post_model_have_correct_object_names(self):
        """Test model Post have correct object name."""
        self.assertEqual(
            str(self.post),
            self.post.text[:15]
        )

    def test_models_have_verbose_name(self):
        """Test verbose_name."""
        field_verboses = {
            'text': 'Текст поста',
            'group': 'Группа',
            'author': 'Автор',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.post._meta.get_field(field).verbose_name,
                    expected_value
                )

    def test_models_have_help_text(self):
        """Test help_text."""
        field_help_texts = {
            'text': 'Введите текст поста',
            'group': 'Укажите название вашей группы'
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.post._meta.get_field(field).help_text,
                    expected_value
                )


class GroupModelTest(TestData):
    """Group model testing."""
    def test_models_have_correct_object_names(self):
        """Test model Group have correct object name."""
        self.assertEqual(str(self.group), self.group.title)


class CommentModelTest(TestData):
    """Comment model testing."""
    def test_comment_model_have_correct_object_names(self):
        """Test model Comment model have correct object name."""
        self.assertEqual(
            str(self.comment_post),
            self.comment_post.text[:15]
        )

    def test_comment_model_have_verbose_name(self):
        """Test comment model have verbose_name."""
        self.assertEqual(
            self.comment_post._meta.get_field('text').verbose_name,
            'Текст',
        )

    def test_comment_model_have_help_text(self):
        """Test comment model have help_text."""
        self.assertEqual(
            self.comment_post._meta.get_field('text').help_text,
            'Текст нового комментария'
        )
