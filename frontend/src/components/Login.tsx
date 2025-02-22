import React from "react";

const Login: React.FC = () => {
    const handleGithubLogin = () => {
        window.location.href = "http://localhost:8000/auth/github/login/";
    };

    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-2xl mb-4">Login to Continue</h1>
            <button 
                className="px-4 py-2 bg-black text-white rounded" 
                onClick={handleGithubLogin}
            >
                Login with GitHub
            </button>
        </div>
    );
};

export default Login;
