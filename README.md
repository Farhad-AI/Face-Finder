# Face Finder! Detecting, analyzing and filtering faces
This project consists of 3 steps: First of all, detecting faces available in the image, then analyzing these faces by a dedicated network to get their attributes and finaly, filter them to truncate the final list and show the result. 

### Examples

        img_copy = face_finder(address, gender='man'                  
![man](https://user-images.githubusercontent.com/106428795/184708598-8fb701fa-0805-458d-87e5-f999de59c037.jpg)

        img_copy = face_finder(address, gender='woman' )
![women](https://user-images.githubusercontent.com/106428795/184708614-c01e4a73-35ce-4e32-8065-fa493aac5398.jpg)

        img_copy = face_finder(address, gender='woman' , age_min=35)
![woman-age](https://user-images.githubusercontent.com/106428795/184708634-4da36f1b-0e1e-4f22-846c-c54594f7aeab.jpg)

        img_copy = face_finder(address, race='asian' )
![asian](https://user-images.githubusercontent.com/106428795/184708655-dafb3413-ee68-4015-8b7e-be9b0aa86e53.jpg)

        img_copy = face_finder(address, race='Black' )
![black](https://user-images.githubusercontent.com/106428795/184708690-04a244c7-ff8b-4f87-a7ef-a678655fce07.jpg)

        img_copy = face_finder(address, gender='man', race='black' )
![black-man](https://user-images.githubusercontent.com/106428795/184708709-b05210ef-0116-4579-a3c9-ff25b34d1e51.jpg)

