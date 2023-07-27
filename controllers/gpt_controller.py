from flask import request, jsonify
import openai
import config

openai.api_key = config.OPENAI_APIKEY

def index():
    return jsonify({'message': "Welcome to ChatGPT!"})

def genresult(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[

            {"role": "user", "content": prompt}
        ]
    )
    result = response['choices'][0]['message']['content'].strip()
    return result

def generate():
    data = request.get_json()
    department = data.get('department', None)
    user_message = data['message']
    
    if department:
        context = f"I'm interested only in {department}."
    else:
        context = "I'm going to tell you about general things."

    # if 'Marketing'.lower() in department.lower():
    #     context = "I'm interested only in marketing."
    # elif department == 'Human Resources':
    #     context = "You are a human resources expert."
    # elif department == 'Sales':
    #     context = "You are a sales expert."
    # else:
    #     context = "You are an AI developed by OpenAI."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        presence_penalty=-2,
        frequency_penalty=2,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": user_message},
        ]
    )

    result = response['choices'][0]['message']['content'].strip()
    return jsonify({'message': result})
    
# @app.route('/generateColdEmail', methods=['POST'])
def generateColdEmail():
    data = request.get_json()['content']
    product_a = data['product_a']
    purpose_a = data['purpose_a']
    prompt = f"Craft a cold email for {purpose_a}. Its product / service: {product_a} highlighting."
    
    res = genresult(prompt)
    return jsonify({"email": res})

# @app.route('/generateSubjectLines', methods=['POST'])
def generateSubjectLines():
    data = request.get_json()['content']
    product_a = data['product_a']
    keywords = data['keywords']

    prompt= f"Create compelling email subject lines for {product_a} with Keywords: {keywords}"
    
    res = genresult(prompt)
    return jsonify({"subject_lines": res})

# @app.route('/generateSalesStrategy', methods=['POST'])
def generateSalesStrategy():
    data = request.get_json()['content']
    product_a = data['product_a']
    audience_a = data['audience_a']
    goal_a = data['goal_a']
    prompt = f"Develop a sales strategy for this product: {product_a}, which is designed to {goal_a}. The target audience for the sales strategy is {audience_a}"
    
    res = genresult(prompt)
    return jsonify({"sales_strategy": res})

# @app.route('/generateSalesProposal', methods=['POST'])
def generateSalesProposal():
    data = request.get_json()['content']
    product_a = data['product_a']
    audience_a = data['audience_a']
    prompt = "Create a compelling sales proposal to purchase our product "+product_a+"The target audience for the sales strategy is"+audience_a
    res = genresult(prompt)
    return jsonify({"sales_proposal": res})

# @app.route('/generateBlogTitles', methods=['POST'])
def generateBlogTitles():
    data = request.get_json()
    description = data['description']
    keywords = data['keywords']
    
    prompt = f"Create 6 best blog titles about this description: {description}, Keywords: {keywords}\
            Give the list of titles to me with bullets, line by line at each titles without \", and each Title must be started with Upper case."
    res = genresult(prompt).split("\n")
    return jsonify({"titles": res})

# @app.route('/generateBlogArticle', methods=['POST'])
def generateBlogArticle():
    data = request.get_json()
    title = data['title']
    keywords = data['keywords']
    tone = data['tone']
    length = data['length']
    
    prompt = f"Create the best blog articles about this title: {title}, Keywords: {keywords}, Tone: {tone}\
            The number of words in the entire articles must be around {length} and not show word numbers"
    
    res = genresult(prompt)
    return jsonify({"article": res})

# @app.route('/generateArticle', methods=['POST'])
def generateArticle():
    data = request.get_json()
    topic_a = data['topic']
    subtitle_a = data['subtitle']
    if len(data['title']) > 0:
        title_a =  "with this title: "+data['title']+" "
    else:
        title_a = ""
    keypoints_a = data['keypoints']
    subtopics_a = data['subtopics']
    facto_a = data['facto']
    examples_a = data['examples']
    prompt = "Create a compelling article"+title_a+" about "+topic_a+" with this subtitle: "+ subtitle_a+" . The key points of this article will be : "+keypoints_a+" and some of the subtopics will be: "+subtopics_a+". The article has to be "+facto_a+" and include this example: "+examples_a+" Give the article to me with these guidelines: 1- It has to be in an HTML Format (Don't include <html>,<head> or <body>, just the <div>) 2- Add <br> Tags after each title and paragraph 3- Don't add any CSS 4- Don't add Images 5- Add <b> tags to highlight content"     
    return genresult(prompt)

# @app.route('/generateWebHeadline', methods=['POST'])
def generateWebHeadline():
    data = request.get_json()
    description = data['description']
    primaryKeywords = data['primaryKeywords']
    tone = data['tone']

    prompt = f"Create compelling headlines for a website about {description} with Keywords: {primaryKeywords}, Tone: {tone}"
    
    res = genresult(prompt)
    return jsonify({"headline": res})

# @app.route('/generateDigitalAd', methods=['POST'])
def generateDigitalAd():
    data = request.get_json()['content']
    product_a = data['product_a']
    data = request.get_json()
    description = data['description']
    tone = data['tone']
    prompt = f"Create compelling digital ads for this product: {product_a}, with this description: {description}, Tone: {tone}"
    res = genresult(prompt)
    return jsonify({"digital_ad": res})

# @app.route('/generateProductDescription', methods=['POST'])
def generateProductDescription():
    data = request.get_json()['content']
    product_a = data['product_a']
    data = request.get_json()
    description = data['description']    
    tone = data['tone']

    prompt = f"Create compelling product description for this product: {product_a}, with this description: {description}, Tone: {tone}"
    res = genresult(prompt)
    return jsonify({"product_description": res})


# @app.route('/generateMarketingStrategy', methods=['POST'])
def generateMarketingStrategy():
    data = request.get_json()['content']
    product_a = data['product_a']
    audience_a = data['audience_a']
    goal_a = data['goal_a']

    prompt = "Tell me how I should approach the marketing for this product: " + product_a+", this strategy is targeted towards "+audience_a+" . The goal of this strategy is to "+goal_a
    
    res = genresult(prompt)
    return jsonify({"strategy": res})

# @app.route('/generateLandingPageContent', methods=['POST'])
def generateLandingPageContent():
    data = request.get_json()['content']
    product_name = data['product_name']
    data = request.get_json()
    description = data['description']
    tone = data['tone']

    prompt = f"Create compelling Landing Page Content for this product: {product_name}, with this description: {description}, Tone: {tone}"
    
    res = genresult(prompt)
    return jsonify({"landing_page_content": res})

# @app.route('/generateSocialMediaPost', methods=['POST'])
def generateSocialMediaPost():
    data = request.get_json()['content']
    product_a = data['product_a']
    data = request.get_json()
    description = data['description']
    tone = data['tone']

    prompt = f"Create compelling social media for this product: {product_a}, with this description: {description}, Tone: {tone}"

    res = genresult(prompt)
    return jsonify({"social_media": res})

# @app.route('/generatePressRelease', methods=['POST'])
def generatePressRelease():
    data = request.get_json()['content']
    describe_company = data['describe_company']
    company_a = data['company_a']
    data = request.get_json()
    description = data['description']
    tone = data['tone']

    prompt = f"Create compelling Press Release for this company: {describe_company}, with this : {company_a}, and commpany description: {description},  Tone: {tone}"

    res = genresult(prompt)
    return jsonify({"press_release": res})

# @app.route('/generateNewsletterPost', methods=['POST'])
def generateNewsletterPost():
    data = request.get_json()['content']
    describe_company = data['describe_company']
    company_a = data['company_a']
    data = request.get_json()
    description = data['description']
    tone = data['tone']

    prompt = f"Create compelling news letter for this company: {describe_company}, with this : {company_a}, and commpany description: {description},  Tone: {tone}"

    res = genresult(prompt)
    return jsonify({"news_letter": res})

# @app.route('/generateJobDescription', methods=['POST'])
def generateJobDescription():
    data = request.get_json()['content']
    describe_company = data['describe_company']
    main_point = data['main_point']

    prompt = "Create a job description for this: "+main_point+" , the company's description is "+ describe_company

    res = genresult(prompt)
    return jsonify({"job_desc": res})

# @app.route('/generateHiringResearch', methods=['POST'])
def generateHiringResearch():
    data = request.get_json()['content']
    main_point = data['main_point']

    prompt = "I need people in my company, main point is " + main_point

    res = genresult(prompt)
    return jsonify({"research": res})

# @app.route('/generatePerformanceEvaluation', methods=['POST'])
def generatePerformanceEvaluation():
    data = request.get_json()['content']
    position_a = data['position_a']
    name_a = data['name_a']

    prompt = "Generate a performance evaluation for a worker of my company called "+name_a+", their position is "+position_a
    res = genresult(prompt)
    return jsonify({"evaluation": res})

# @app.route('/generatePolicyDesign', methods=['POST'])
def generatePolicyDesign():
    data = request.get_json()['content']
    goal_a = data['goal_a']
    company_mission = data['company_mission']
    
    prompt = "Generate a new policy for my company, the goal is "+goal_a+", company mission is " +company_mission

    res = genresult(prompt)
    return jsonify({"policy_design": res})


# @app.route('/generateHiringLetter', methods=['POST'])
def generateHiringLetter():
    data = request.get_json()
    name_a = data['name']
    position_a = data['position']
    company_a = data['company']
    date_a = data['date']

    prompt = "Generate a hiring letter, the name of the employee is "+name_a+", the position the employee will be occupying "+position_a+" ,  the name of my company is "+company_a+", the expected date for the employee to start is "+date_a+". Give this to me with these guidelines: 1- It has to be in an HTML Format (Don't include <html>,<head> or <body>, just the <div>) 2- Add <br> Tags after each title and paragraph 3- Don't add any CSS 4- Don't add Images 5- Add <b> tags to highlight content"

    return genresult(prompt)

# @app.route('/generateDiversityImprovement', methods=['POST'])
def generateDiversityImprovement():
    data = request.get_json()['content']
    main_point = data['main_point']

    prompt = "I want to improve diversity in my company, this is the current state of diversity in my company:" +main_point

    res = genresult(prompt)
    return jsonify({"improvement": res})

# @app.route('/generateTerminationLetter', methods=['POST'])
def generateTerminationLetter():
    data = request.get_json()['content']
    name_a = data['name']
    position_teminate = data['position_teminate']
    
    prompt = "Generate a termination letter for an employee of my company called "+name_a+", the position of the employee is "+position_teminate

    res = genresult(prompt)
    return jsonify({"termination_letter": res})

# @app.route('/generateHireLetter', methods=['POST'])
def generateHireLetter():
    data = request.get_json()['content']
    hire_position = data['hire_position']
    name_a = data['name_a']

    prompt = "Generate the letter for hire anyone whose position is " + hire_position + ", employer name is " + name_a
    res = genresult(prompt)
    return jsonify({"hire_letter": res})

# @app.route('/generateRecruitmentStrategy', methods=['POST'])
def generateRecruitmentStrategy():
    data = request.get_json()['content']
    main_point = data['main_point']

    prompt = "How can I do a recruitment strategy for my company, main point is " + main_point
    res = genresult(prompt)
    return jsonify({"recruitment_strategy": res})