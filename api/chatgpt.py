from flask import Blueprint

from controllers.gpt_controller import *

chatgpt_bp = Blueprint('chatgpt_bp', __name__)

chatgpt_bp.route('/',  methods =['GET', 'POST'])(index)
chatgpt_bp.route('/generate',  methods =['POST'])(generate)
# Marketing generate
chatgpt_bp.route('/generateBlogTitles',  methods =['POST'])(generateBlogTitles)
chatgpt_bp.route('/generateBlogArticle',  methods =['POST'])(generateBlogArticle)
chatgpt_bp.route('/generateWebHeadline',  methods =['POST'])(generateWebHeadline)
chatgpt_bp.route('/generateDigitalAd',  methods =['POST'])(generateDigitalAd)
chatgpt_bp.route('/generateProductDescription',  methods =['POST'])(generateProductDescription)
chatgpt_bp.route('/generateMarketingStrategy',  methods =['POST'])(generateMarketingStrategy)
chatgpt_bp.route('/generateLandingPageContent',  methods =['POST'])(generateLandingPageContent)
chatgpt_bp.route('/generateSocialMediaPost',  methods =['POST'])(generateSocialMediaPost)
chatgpt_bp.route('/generateNewsletterPost',  methods =['POST'])(generateNewsletterPost)
chatgpt_bp.route('/generatePressRelease',  methods =['POST'])(generatePressRelease)

chatgpt_bp.route('/generateColdEmail',  methods =['POST'])(generateColdEmail)
chatgpt_bp.route('/generateSubjectLines',  methods =['POST'])(generateSubjectLines)
chatgpt_bp.route('/generateSalesStrategy',  methods =['POST'])(generateSalesStrategy)
chatgpt_bp.route('/generateSalesProposal',  methods =['POST'])(generateSalesProposal)
chatgpt_bp.route('/generateJobDescription',  methods =['POST'])(generateJobDescription)
chatgpt_bp.route('/generateHiringResearch',  methods =['POST'])(generateHiringResearch)
chatgpt_bp.route('/generatePerformanceEvaluation',  methods =['POST'])(generatePerformanceEvaluation)
chatgpt_bp.route('/generatePolicyDesign',  methods =['POST'])(generatePolicyDesign)
chatgpt_bp.route('/generateHireLetter',  methods =['POST'])(generateHireLetter)
chatgpt_bp.route('/generateDiversityImprovement',  methods =['POST'])(generateDiversityImprovement)
chatgpt_bp.route('/generateTerminationLetter',  methods =['POST'])(generateTerminationLetter)
chatgpt_bp.route('/generateRecruitmentStrategy',  methods =['POST'])(generateRecruitmentStrategy)