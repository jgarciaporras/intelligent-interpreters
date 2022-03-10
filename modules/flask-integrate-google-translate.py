#@app.route("/", methods=["POST"])
def translator():
    if request.method == "POST":
        
            #takes transcribed text from function
        transcription = transcribe(audio_path, language)
        language = str(request.form["language"])
        
        
        #translate_function is the function for Google translate api
    translator = translate(transcription, source, target)
    translation = translate.text
    
    return render_template("index.html", language=language, transcription=transcription, translation=translation)


#@app.route("/")
def index():
    lang = [{"name":"English", "language":"en"}, {"name":"Spanish", "language":"es"}, 
            {"name":"German", "language":"de"}, {"name":"Korean", "language":"kr"}, 
            {"name":"Hindi", "language":"hi"}, {"name":"Japanese", "language":"jp"}, 
            {"name":"French", "language":"fr"}, {"name":"Afrikaans", "language":"af"}]
    
    return render_template("index.html", languages=lang)