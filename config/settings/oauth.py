from config.settings import secret

SOCIAL_AUTH_QQ_KEY = secret.SOCIAL_AUTH_QQ_KEY
SOCIAL_AUTH_QQ_SECRET = secret.SOCIAL_AUTH_QQ_SECRET

SOCIAL_AUTH_GITHUB_KEY = secret.SOCIAL_AUTH_GITHUB_KEY
SOCIAL_AUTH_GITHUB_SECRET = secret.SOCIAL_AUTH_GITHUB_SECRET

SOCIAL_AUTH_CODING_KEY = secret.SOCIAL_AUTH_CODING_KEY
SOCIAL_AUTH_CODING_SECRET = secret.SOCIAL_AUTH_CODING_SECRET

AUTHENTICATION_BACKENDS = (
    'social.backends.qq.QQOAuth2',
    'social.backends.github.GithubOAuth2',
    'users.oauth.CodingOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_USER_MODEL = 'users.Oauth'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

SOCIAL_AUTH_GITHUB_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GITHUB_SCOPE = [
    'user'
]


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'

