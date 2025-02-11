from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/nocors')
def no_cors_route():
    return {"message": "CORS is enabled for this route"}

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [
            (1000, "M"), (900, "CM"), 
            (500, "D"), (400, "CD"), 
            (100, "C"), (90, "XC"), 
            (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), 
            (5, "V"), (4, "IV"), 
            (1, "I")
        ]

        result = ''
        for value, symbol in digits:
            if num >= value:
                count = num // value
                result += count * symbol
                num = num % value
        
        return result

@app.route('/convert', methods=['GET'])
def convert():
    try:
        num = int(request.args.get('num'))
        if num <= 0 or num > 3999:
            return jsonify({"error": "Number must be between 1 and 3999"}), 400
        
        solution = Solution()
        roman_numeral = solution.intToRoman(num)
        return jsonify({"number": num, "roman": roman_numeral})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide a valid integer."}), 400

if __name__ == '__main__':
    app.run(debug=True)