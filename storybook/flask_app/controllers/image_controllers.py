from flask_app import app, APIKEY
from flask import render_template, redirect, request, session
import os
import openai
openai.organization = "org-mpaYTEpuV3ebZVgJ0bMZ06X2"
openai.api_key = APIKEY
openai.Model.list()


# ------------- Landing Display Page -------------

@app.route('/')
def homepage():
    return render_template('homepage.html')



# ------------- Landing Display Page -------------
@app.route('/first_page')
def first_page():
    return render_template('story_page_1.html')




# ---------------- PICTURE ACTION AND DISPLAY ROUTES -------------


# ==================================================================
# ------------- PET DRAGON - API REQUEST ROUTE -------------

# Pet Dragon Route
@app.route('/pet_dragon')
def pet_dragon_api_call():
    
    # API CREATE CALL - Stores URL in Results
    results = openai.Image.create(
    prompt="a human petting an enormous scary blue dragon on a castle tower over a medieval city",
    n=1,
    size="1024x1024"
    )
    print(results)

    # Store Results in Session
    img_url = results["data"][0]['url']
    session['pet_dragon_img_url'] = img_url

    print(session['pet_dragon_img_url'])

    return redirect('/story/petdragon')


# ------------- PET DRAGON - API DISPLAY ROUTE -------------
@app.route('/story/petdragon')
def show_pet_dragon_page():
    img_url = session['pet_dragon_img_url']
    return render_template('story_page_pet_dragon.html', img_url=img_url)



# ==================================================================
# ------------- SHOOT ARROW - API REQUEST ROUTE -------------

# Pet Dragon Route
@app.route('/shoot_arrow')
def shoot_arrow_api_call():
    
    # API CREATE CALL - Stores URL in Results
    results = openai.Image.create(
    prompt="a human warrior aiming a bow and arrow at an enormous scary blue dragon on a castle tower over a medieval city",
    n=1,
    size="1024x1024"
    )
    print(results)

    # Store Results in Session
    img_url = results["data"][0]['url']
    session['shoot_arrow_img_url'] = img_url

    print(session['shoot_arrow_img_url'])

    return redirect('/story/shootarrow')


# ------------- SHOOT ARROW - API DISPLAY ROUTE -------------
@app.route('/story/shootarrow')
def show_shoot_arrow_page():
    img_url = session['shoot_arrow_img_url']
    return render_template('story_page_shoot_arrow.html', img_url=img_url)





# ==================================================================
# ------------- RUN AWAY - API REQUEST ROUTE -------------

# Run Away Route
@app.route('/runaway')
def runaway_api_call():
    
    # API CREATE CALL - Stores URL in Results
    results = openai.Image.create(
    prompt="a human warrior running down an alley while an enormous flying scary blue dragon chases them through a medieval city",
    n=1,
    size="1024x1024"
    )
    print(results)

    # Store Results in Session
    img_url = results["data"][0]['url']
    session['runaway_img_url'] = img_url

    print(session['runaway_img_url'])

    return redirect('/story/runaway')


# ------------- SHOOT ARROW - API DISPLAY ROUTE -------------
@app.route('/story/runaway')
def show_runaway_page():
    img_url = session['runaway_img_url']
    return render_template('story_page_runaway.html', img_url=img_url)





# ==================================================================
# ------------- RIDE THE DRAGON - API REQUEST ROUTE -------------

# Ride Dragon Route
@app.route('/ride_dragon')
def riding_dragon_api_call():
    
    # API CREATE CALL - Stores URL in Results
    results = openai.Image.create(
    prompt="human riding an enormous flying scary blue dragon through the sky over a medieval city with mountains in the background",
    n=1,
    size="1024x1024"
    )
    print(results)

    # Store Results in Session
    img_url = results["data"][0]['url']
    session['riding_dragon_img_url'] = img_url

    print(session['riding_dragon_img_url'])

    return redirect('/story/ride_dragon')


# ------------- RIDE DRAGON - API DISPLAY ROUTE -------------
@app.route('/story/ride_dragon')
def show_riding_dragon_page():
    img_url = session['riding_dragon_img_url']
    return render_template('story_page_riding_dragon.html', img_url=img_url)





# # ------------- CONCLUSION DISPLAY ROUTE -------------

@app.route('/ending')
def final_page():
    single_dragon = session['pet_dragon_img_url']
    dragon_path = []
    dragon_path.append(session['pet_dragon_img_url'])
    dragon_path.append(session['riding_dragon_img_url'])
    return render_template('conclusion_page.html', single_dragon=single_dragon, dragon_path=dragon_path)