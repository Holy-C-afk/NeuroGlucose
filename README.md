# NeuroGlucose System

The NeuroGlucose system is a Django web application designed to detect blood sugar variations through eye movement analysis. This innovative approach aims to provide real-time monitoring and automate insulin injections using Raspberry Pi or Arduino integration.

## Features

- **Eye Movement Analysis**: Utilizes advanced algorithms to analyze eye movements for detecting blood sugar variations.
- **Insulin Injection Automation**: Integrates with Raspberry Pi or Arduino to automate insulin delivery based on detected glucose levels.
- **User-Friendly Interface**: Provides an intuitive web interface for users to monitor their glucose levels and manage settings.
- **Real-Time Monitoring**: Offers real-time updates and alerts for blood sugar variations.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/neuroglucose.git
   ```
2. Navigate to the project directory:
   ```
   cd neuroglucose
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the development server:
   ```
   python manage.py runserver
   ```
2. Access the application at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.