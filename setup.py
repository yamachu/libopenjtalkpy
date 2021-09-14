'''Install libopenjtalkpy and download pre-built LibOpenJTalk library
'''

import re
import sys
# import json

from setuptools import setup, find_packages
from setuptools.command.install import install

# http://python-future.org/compatible_idioms.html
try:
    from urllib.request import urlretrieve, urlopen, Request
except ImportError:
    from urllib import urlretrieve
    from urllib2 import urlopen, Request


class LibraryDownloader(install):
    '''Hook base install task and download pre-build LibOpenJTalk library after install
    '''

    _DOWNLOAD_BASE_URL = 'https://github.com/yamachu/LibOpenJTalk/releases/download'
    _LIBRARY_NAME = {
        'mac_32': ('libopenjtalk.dylib', 'libopenjtalk.dylib'),
        'mac_64': ('libopenjtalk.dylib', 'libopenjtalk.dylib'),
        # 全部32bitにしておいた方がバンドルされた時に動かないとかなくていいのかもしれない
        'linux_32': ('libopenjtalk.so', 'libopenjtalk.so'),
        'linux_64': ('libopenjtalk.so', 'libopenjtalk.so'),
        'win_32': ('x86_open_jtalk.dll', 'libopenjtalk_32.dll'),
        'win_64': ('x64_open_jtalk.dll', 'libopenjtalk_64.dll'),
    }


    def _get_base_install_path(self):
        # Path separator Unix is '/', Win is '\'
        pathre = re.compile('libopenjtalkpy.__init__\.py')
        install_base_dir = ''
        for path in install.get_outputs(self):
            if pathre.search(path):
                install_base_dir = path.replace('__init__.py', '')
                break

        return install_base_dir


    def _get_platform(self):
        '''Get current platform

        Returns:
            str: current platform (win, mac, linux) and (32, 64) or ""
        '''

        platform = ''
        if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
            platform = 'win'
        elif sys.platform.startswith('darwin'):
            platform = 'mac'
        elif sys.platform.startswith('linux'):
            platform = 'linux'
        return "{}_{}".format(platform, 64 if sys.maxsize > 2**32 else 32)


    def _get_library(self, platform):
        '''Get native LibOpenJTalk library name

        Args:
            platform (str): current platform

        Returns:
            str: Library file name

        Raises:
            Exception: When current platform not win, mac or linux, throw
        '''
        if platform == 'win_32':
            return 'libopenjtalk_32.dll'
        elif platform == 'win_64':
            return 'libopenjtalk_64.dll'
        elif platform.startswith('mac'):
            return 'libopenjtalk.dylib'
        elif platform.startswith('linux'):
            return 'libopenjtalk.so'
        else:
            raise Exception('This architecture is not supported')


    def _get_install_full_path(self, base_path, library_name):
        return '{}{}'.format(base_path, library_name)


    def run(self):
        install.run(self)

        platform = self._get_platform()
        library_full_path = self._get_install_full_path(
            self._get_base_install_path(),
            self._LIBRARY_NAME[platform][1])

        # get_latest_request = Request('https://github.com/yamachu/LibOpenJTalk/releases/latest',
        #                              headers={'Accept': 'application/json'})
        # get_latest_response = urlopen(get_latest_request)
        # response_str = get_latest_response.read().decode('utf-8')
        # response_json = json.loads(response_str)
        # latest_version = response_json['tag_name']
        latest_version = "v_lib_1.10.28"

        download_url = "{}/{}/{}".format(
            self._DOWNLOAD_BASE_URL,
            latest_version,
            self._LIBRARY_NAME[platform][0])
        urlretrieve(download_url, library_full_path)


    def get_outputs(self):
        return install.get_outputs(self) + [self._get_install_full_path(
            self._get_base_install_path(),
            self._get_library(self._get_platform())),]


setup(
    name="libopenjtalkpy",
    version="0.0.1",
    packages=find_packages(),
    description='Python wrapper for LibOpenJTalk',
    url='https://github.com/yamachu/libopenjtalkpy',
    author='yamachu',
    license='MIT',
    cmdclass={'install': LibraryDownloader},
    keywords='libopenjtalk, libopenjtalkpy',
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
    ]
)
