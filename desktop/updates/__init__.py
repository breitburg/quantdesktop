from os import getcwd
from platform import system
from logging import critical
from logging import info
from webbrowser import open as openurl
from github.GithubException import RateLimitExceededException
from desktop.uis import messagebox


try:
    from github import Github

    api = Github()
    release = api.get_repo('breitburg/quantify-desktop').get_latest_release()
except RateLimitExceededException:
    pass

path = getcwd()


def check_new():
    from setup import __version__
    return release.tag_name != __version__


def check_updates():
    while True:
        if not check_new(): continue
        info(f'Обновление! ({release.tag_name})')
        assets = release.get_assets()
        url = assets.get_page(0)[0].browser_download_url

        result = messagebox.askquestion('Обновление', f'Доступна новая версия ({release.tag_name})!\n'
        f'Хотите скачать обновление?', icon='warning')
        if result == 'yes':
            openurl(url=url)
            quit()