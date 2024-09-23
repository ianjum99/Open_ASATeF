# Open AI Stress Testing Framework
The AI Stress-Testing Framework is an application designed to evaluate and improve the reliability, safety, and effectiveness of AI models. 



## Purpose

- Test AI models: The framework allows you to stress-test various AI models by presenting them with challenging scenarios.
- Verify honesty and reliability: It helps identify potential issues in AI responses, such as inconsistencies, biases, or incorrect information.
- Measure safeguard effectiveness: The application evaluates how well the AI models handle ethical considerations, content filtering, and uncertainty.
- Improve AI systems: By identifying weaknesses and areas for improvement, the framework helps in refining AI models.


## How to use it

1. Access the Dashboard: When you open the application, you'll see a dashboard with several sections.
2. Run New Tests:

  a. In the "Run New Test" section, you can input a scenario type and content.
  b. For example, you might enter "Ethical Dilemma" as the scenario type and describe a complex ethical situation in the content field.
  c. Click "Run Test" to submit this scenario to the AI models.


3. View Safeguard Effectiveness:
  
  1. The dashboard displays a chart showing the effectiveness of various safeguards (e.g., content filtering, ethical reasoning).
  2. This gives you an overview of how well the AI models are performing in different aspects of safety and reliability.
  

4. Analyze Test Results:

  1. In the "Recent Test Results" section, you can view the outcomes of your tests.
  2. For each test, you'll see:
  
     a. The timestamp of when the test was run
     b. The scenario content
     c. Issues identified for different AI models
     d. Any human verification that has been added


5. Human-AI Collaboration:

  1. The framework includes a feature for humans to verify and provide feedback on AI responses.
  2. This helps in improving the accuracy of the system and provides a way to correct any mistakes made by the AI.


6. Iterate and Improve:

  1. Based on the test results and safeguard effectiveness metrics, you can identify areas where the AI models need improvement.
  2. You can then work on refining the AI models, adjusting their training data, or modifying their underlying algorithms to address the identified issues.


7. Monitor Progress:

  1. By running tests regularly and comparing results over time, you can track the progress and improvements in your AI models' performance and safety.

## Setup Instructions

### Backend Setup

1. Navigate to the project root directory.

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a `.env` file in the root directory.
- Add your OpenAI API key: 
```
OPENAI_API_KEY=your_api_key_here`
```

5. Initialize the database:
```
python backend/database.py

```


6. Run the backend application:
``` 
python backend/main.py
```



### Frontend Setup

1. Navigate to the frontend directory:

```
cd frontend
```

2. Install the required npm packages:
```
npm install
```

3. Start the development server:
```

npm start

```

## Usage Guide

1. Access the dashboard by opening a web browser and navigating to 
```
`http://localhost:3000`.
```

2. Use the Human-AI Collaboration interface to submit claims for verification:
- Enter a claim in the input field.
- Click "Submit Claim" to send it to the AI model for verification.
- Review the AI's response and provide your own verification.

3. View test results and safeguard effectiveness in the dashboard:
- The "Safeguard Effectiveness" chart displays scores for various AI safeguards.
- The "Recent Test Results" table shows the latest AI model responses and human verifications.

4. To run a new batch of tests, use the backend CLI:
```
python backend/main.py --generate-scenarios 50 --run-tests

```

## Contributing

We welcome contributions to the AI Stress-Testing Framework! Here's how you can help:

1. Fork the repository and create your feature branch.
2. Implement your changes, adhering to the existing code style.
3. Write or update tests as necessary.
4. Update the documentation to reflect your changes.
5. Submit a pull request with a clear description of your improvements.

## License

This project is licensed under the MIT License.

## Contact

For questions, suggestions, or support, please open an issue on our GitHub repository or contact the maintainers at [ibrahimanjum15@gmail.com](mailto:ibrahimanjum15@gmail.com).

## Acknowledgments

- OpenAI for providing the GPT models used in this project.
- Hugging Face for their transformers library and model hub.
- The open-source community for various libraries and tools used in this project.

Thank you for your interest in the AI Stress-Testing Framework. Together, we can work towards more reliable and ethical AI systems!
