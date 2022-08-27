# Face finder! Detecting, analyzing and filtering faces
This project consists of 3 steps: First of all, detecting faces available in the image, then analyzing these faces by a dedicated network to get their attributes and finaly, filtering them in order to truncate the final list and show the result. 

### Examples

        img_copy = face_finder(address, gender='man' )                  
![man](https://user-images.githubusercontent.com/106428795/184708598-8fb701fa-0805-458d-87e5-f999de59c037.jpg)

        img_copy = face_finder(address, gender='woman' )
![women](https://user-images.githubusercontent.com/106428795/184708614-c01e4a73-35ce-4e32-8065-fa493aac5398.jpg)

        img_copy = face_finder(address, gender='woman' , age_min=35)
![woman-age](https://user-images.githubusercontent.com/106428795/184708634-4da36f1b-0e1e-4f22-846c-c54594f7aeab.jpg)

        img_copy = face_finder(address, race='asian' )
![asian](https://user-images.githubusercontent.com/106428795/187023821-03702b62-59cf-4ca8-9326-30994e345f3a.jpg)


        img_copy = face_finder(address, race='Black' )
![black](https://user-images.githubusercontent.com/106428795/187023834-f6b33915-113c-4ee4-9a97-431e56ca5aac.jpg)


        img_copy = face_finder(address, gender='man', race='black' )
![black man](https://user-images.githubusercontent.com/106428795/187023848-776078c0-df7e-4a0d-aba5-c7f82517121a.jpg)


