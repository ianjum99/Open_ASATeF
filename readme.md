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

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more detailed information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or support, please open an issue on our GitHub repository or contact the maintainers at [ibrahimanjum15@gmail.com](mailto:ibrahimanjum15@gmail.com).

## Acknowledgments

- OpenAI for providing the GPT models used in this project.
- Hugging Face for their transformers library and model hub.
- The open-source community for various libraries and tools used in this project.

Thank you for your interest in the AI Stress-Testing Framework. Together, we can work towards more reliable and ethical AI systems!
```
