import os
import requests
def MarsImage():

    name = 'curiosity'

    date = '2020-12-3'
    Api_Key = 'H4lRQndBC0EgmA9IAc7Wb1i4TKNBIIKZ0d3hilQv'
    Api_ = Api_Key

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:3]

    try:
        for index , photo in enumerate(Photos):
            camera = photo["camera"]
            rover = photo["rover"]

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)
            Path_1 = "C:\\Users\\Hp\\PycharmProjects\\pythonProject1\\"+str(img)
            Path_2 = "C:\\Users\\Hp\\PycharmProjects\\pythonProject1\\Jarvis\\Nasa Database\\"+str(img)

            os.rename(Path_1,Path_2)

            # os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            print(f"This Image was captured with : {full_camera_name}")
            print(f"This Image was captured on : {date_of_photo} ")
    except:
        print("There is an error!")
MarsImage()