import grequests
from time import sleep
from parsel import Selector
from face_detection import FaceDetector


def fetch_content(list_of_dicts):
    git_urls = ['https://github.com/' + each_dict['github_username'] for each_dict in list_of_dicts]
    readme_urls = ['https://github.com/' + each_dict['github_username'] + '/' + each_dict['github_username'] for each_dict in list_of_dicts]
    
    git_gen = (grequests.get(git) for git in git_urls)
    readme_gen = (grequests.get(readme) for readme in readme_urls)

    git_responses = grequests.map(git_gen)
    readme_responses = grequests.map(readme_gen)

    for index in range(len(list_of_dicts)):
        list_of_dicts[index]['github'] = Selector(text=git_responses[index].text)
        list_of_dicts[index]['github_readme'] = Selector(text=readme_responses[index].text)
    
    photos_urls = [selector['github'].css('a[itemprop="image"]::attr(href)').get() for selector in list_of_dicts ]

    photo_gen = (grequests.get(photo) for photo in photos_urls)
    photo_responses = grequests.map(photo_gen)

    sleep(1)

    for index in range(len(list_of_dicts)):
        with open('photos/'+ list_of_dicts[index]['github_username']+'_image.jpg', 'wb') as handler:
            handler.write(photo_responses[index].content) 
        list_of_dicts[index]['photo'] = FaceDetector.find_faces('photos/'+ list_of_dicts[index]['github_username'] +'_image.jpg')

    return list_of_dicts