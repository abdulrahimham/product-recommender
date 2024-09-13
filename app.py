from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Route to handle product recommendation
@app.route('/recommend', methods=['GET'])
def recommend():
    # Get product_id from the user query parameter
    product_id = request.args.get('product_id')
    
    # If product_id is not provided, return an error message
    if not product_id:
        return jsonify({"error": "Product ID not provided"}), 400
    
    # Mock function to return recommendations (replace this with the actual recommendation logic)
    def get_refined_recommendations(product_id):
        # Mock recommendations
        return ['B001', 'B002', 'B003'], ['Great product!', 'Good, but...', 'Average']
    
    # Get recommendations for the provided product ID
    recommended_products, review_summaries = get_refined_recommendations(product_id)
    
    # Format the results as a list of dictionaries
    results = [{"product_id": pid, "review_summary": summary} for pid, summary in zip(recommended_products, review_summaries)]
    
    # Return the recommendations as JSON
    return jsonify(results)

# If running locally, start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
