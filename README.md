# CardiScan: Heart Disease Prediction Dashboard

CardiScan is a professional-grade, AI-powered medical dashboard inspired by the Streamlit aesthetic. It leverages the UCI Heart Disease dataset to provide researchers and healthcare professionals with interactive data visualizations and predictive risk assessments using Gemini AI.

## 🚀 Features

- **Data Overview**: High-level metrics and global distributions of the heart disease dataset.
- **Detailed Analysis**: Interactive charts exploring correlations between cholesterol, age, and blood pressure.
- **Smart Predictor**: An AI-driven diagnostic tool that analyzes custom user parameters to assess risk levels.
- **Streamlit Interface**: A custom-built React UI that replicates the clean, technical look of Streamlit.

## 🛠️ Technology Stack

- **Frontend**: React 19, Vite, Tailwind CSS 4
- **Visualization**: Recharts, Lucide Icons
- **AI Engine**: Google Gemini 2.0 (via `@google/genai`)
- **Animations**: Motion (formerly Framer Motion)

## 📦 Installation

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   npm install
   ```
3. **Set up environment variables**
   Create a `.env` file and add your Gemini API Key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
4. **Run the development server**
   ```bash
   npm run dev
   ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Credits

Developed by **Manoj g**.
