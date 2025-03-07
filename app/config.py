import os

# Пути к медиафайлам
MEDIA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')

VIDEOS = {
    'welcome': os.path.join(MEDIA_PATH, 'welcome_video.mp4'),
}
