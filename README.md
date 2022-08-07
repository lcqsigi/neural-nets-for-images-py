# neural-nets-for-images-py

# Setup the enviroment and install needed dependencies

`conda create -n neural-env python=3.9`  
`conda activate neural-env`  
`pip install -r requirements.txt`  

# How to use the code

To execute the code, open a terminal and type:
 
```sh
cd app
 python neural_net.py
cd ..
```

This code could also be accessed from a web browser: `https://rsc468-neural.herokuapp.com/` 

The idea behind this development is that of using a previously trained
`pytorch` model (e.g., `frcnn0906.pth`) to classify user provided images of
cats and dogs contained in a file named: `file.tar`

# Contents of the file.tar

`cat.2450.jpg`  
`cat.2451.jpg`  
`cat.2452.jpg`  
`cat.2453.jpg`  
`cat.2454.jpg`  
`cat.2455.jpg`  
`cat.2456.jpg`  
`cat.2457.jpg`  
`cat.2458.jpg`  
`cat.2459.jpg`  
`dog.2450.jpg`  
`dog.2451.jpg`  
`dog.2452.jpg`  
`dog.2453.jpg`  
`dog.2454.jpg`  
`dog.2455.jpg`  
`dog.2456.jpg`  
`dog.2457.jpg`  
`dog.2458.jpg`  
`dog.2459.jpg`  

`NOTE:`
    + The model `frcnn0906.pth` was created separately with the use of a `GPU`
      infrastructure and it has an accuracy of 90% on the `validation` set
    + High-resolution images could not be tested on the `Heroku Platform`
      because the execution of the APP  may pass the allowed runtime.
    + The format of the `file.tar` is set to receive 20 images in total
      splitted evenly for dogs and cats (see above).
    + The `file.tar` can be created using Unix syntax (e.g., `tar -cf file.tar`
      dog*.jpg cat*.jpg`). This file can be either be uploaded if using the web
      app or saved in the `main` path of this repository:
      `git@github.com:lcqsigi/neural-nets-for-images-py.git`
