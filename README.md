# quickdraw-image-generation

quickdraw-image-generation.py script generates JPEG files from QuickDraw binary files for further use in [Create ML] application.  
It allows you to specify the number of images generated for each QuickDraw category for training and testing purposes.

How to use:

- add binary_file_parser.py [file]
- copy necessary files from the "quickdraw_dataset" Google Cloud [storage]
- install dependencies: [PIL]
- run `python3 ./quickdraw-image-generation.py`
- The result JPEG files will be stored in `output/training/` and `output/testing/` folders
- Drag-and-drop folder to [Create ML] application, generate a model
- Use the result in iOS application

Usage example: [doodle-recognizer project]

[create ml]: https://developer.apple.com/machine-learning/create-ml/
[file]: https://github.com/googlecreativelab/quickdraw-dataset
[storage]: https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/binary;tab=objects?pli=1&prefix=&forceOnObjectsSortingFiltering=false
[pil]: https://github.com/python-pillow/Pillow
[doodle-recognizer project]: https://github.com/petr-lazarev/doodle-recognizer
