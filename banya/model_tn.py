from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class ProjectDataSort(models.Model):
    project_data_sort_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'project_data_sort'  # 실제 테이블 이름을 지정합니다.

    def __str__(self):
        return self


class ArtifactSort(models.Model):
    artifact_sort_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'artifact_sort'  # 실제 테이블 이름을 지정합니다.

    def __str__(self):
        return self


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.TextField()
    project_sort = models.IntegerField()
    project_data_sort = models.IntegerField()
    artifact_selected = models.CharField(max_length=10)
    banya_api_key = models.TextField()
    thum_image_url = models.CharField(max_length=100)
    user_email = models.CharField(max_length=254)
    created_date = models.DateTimeField()

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self


class ProjectDetailReady(models.Model):
    source = models.TextField()
    id = models.IntegerField(primary_key=True)
    artifact_sort_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'project_detail_ready'

    def __str__(self):
        return self


class UserApi(models.Model):
    user_email = models.CharField(max_length=254)
    api_key = models.TextField()
    public_key = models.TextField()
    created_date = models.DateTimeField()
    key_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_api'

    def __str__(self):
        return self


class UserBucket(models.Model):
    user_email = models.CharField(max_length=254)
    project_id = models.IntegerField()
    bucket_timestamp = models.DateTimeField()
    file_url = models.CharField(max_length=2000)

    class Meta:
        db_table = 'user_bucket'

    def __str__(self):
        return self


class TrainedModel(models.Model):
    name = models.CharField()
    size = models.IntegerField()
    model_sort = models.IntegerField()
    model_url = models.CharField(max_length=500)
    training_status = models.IntegerField()
    time_taken = models.IntegerField()
    created_date = models.DateTimeField()
    project_id = models.IntegerField()
    user_email = models.EmailField(max_length=254)
    bucket_timestamp = models.DateTimeField()

    class Meta:
        db_table = 'trained_model'

    def __str__(self):
        return self


class ModelSettings(models.Model):
    setting_name = models.CharField(max_length=100)
    language_sort = models.IntegerField()
    words_limit = models.IntegerField()
    img_count_limit = models.IntegerField()
    self_speech_strength = models.IntegerField()
    img_use_strength = models.IntegerField()
    standard_knowledge_strength = models.IntegerField()
    creativity_strength = models.IntegerField()
    created_time= models.DateTimeField()
    project_id = models.IntegerField()
    user_email = models.IntegerField()

    class Meta:
        db_table = 'model_settings'

    def __str__(self):
        return self