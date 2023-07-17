from flask import Flask, request,jsonify
import os
from werkzeug.utils import secure_filename
import uuid


app = Flask(__name__)

@app.route('/transcript', methods=['POST','GET'])
def upload_audio():
    taskid = str(uuid.uuid4())
    if request.method == "POST":
        file = request.files['audio']
        filename = secure_filename(file.filename)
        filename_without_ext=os.path.splitext(filename)[0]

        isExist = os.path.exists("./uploads")
        if(isExist==False):
            os.makedirs("./uploads")

        folder_for_each_video="./uploads/"+taskid
        folder_for_each_video1="uploads/"+taskid
        folder_for_each_video = folder_for_each_video.replace(' ','')
        folder_for_each_video = folder_for_each_video.replace('_','')
        folder_for_each_video1 = folder_for_each_video1.replace(' ','')
        folder_for_each_video1 = folder_for_each_video1.replace('_','')
        isExist = os.path.exists(folder_for_each_video)
        if(isExist==False):
            os.makedirs(folder_for_each_video)

        file.save(os.path.join(folder_for_each_video+"/", filename))
# python3 app/whisperX/local_server_copy.py /home/kcdh/Documents/ASR/Medical/Data/whisperX/output_1.wav
        cmd1 = "python3 whisperX/local_server_copy.py" + " ./" + folder_for_each_video1 + "/" + filename + " ./" + folder_for_each_video1
        os.system(cmd1)
        # sr = "en"
        # dt = "hi"
        # cmd2 = "cd ../indicTrans_model_files/indicTrans/ && " + "bash /home/kcdh/akshay/speechtospeech/ML_Models/indicTrans_model_files/indicTrans/joint_translate.sh"+" /home/kcdh/akshay/speechtospeech/ML_Models/app/" + folder_for_each_video1 +"/"+ filename_without_ext + ".txt" + " /home/kcdh/akshay/speechtospeech/ML_Models/app/"+ folder_for_each_video1 + "/" + "output.txt" + " "+ sr + " " + dt + " /home/kcdh/akshay/speechtospeech/ML_Models/indicTrans_model_files/en-indic/"
        # os.system(cmd2)
        text_file_path = "./" + folder_for_each_video1 + "/recording.txt"
        with open(text_file_path, 'r', encoding='utf-8') as tfp:
            context = tfp.read()
        return context

    # return 'No audio file provided.', 400
    
if __name__ == '__main__':
    app.run()
