from flask import Flask, request, jsonify
from app.analysis import analyze_sentiment, extract_key_points
from app.models import db, Review

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Endpoint untuk menganalisis review
@app.route('/api/analyze-review', methods=['POST'])
def analyze_review():
    data = request.get_json()
    review_text = data.get('review_text', '')
    
    sentiment = analyze_sentiment(review_text)
    key_points = extract_key_points(review_text)
    
    # Menyimpan review ke dalam database
    new_review = Review(review_text=review_text, sentiment=sentiment, key_points=key_points)
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify({"message": "Review analyzed successfully", "review": {"sentiment": sentiment, "key_points": key_points}}), 201

# Endpoint untuk mengambil semua review
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    reviews_data = [{"id": review.id, "review_text": review.review_text, "sentiment": review.sentiment, "key_points": review.key_points} for review in reviews]
    
    return jsonify(reviews_data)

if __name__ == '__main__':
    app.run(debug=True)
