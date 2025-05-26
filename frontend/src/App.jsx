import { useState } from 'react'
import api from './api'
import Profile from './assets/Profile_picture.jpg'


function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  
  // to post question(=text) to api and get answer
  const handleSubmit = async (text) => {
    try {
      const res = await api.post("/", { question: text });
      setResponse(res.data.message);
    } catch (err) {
      console.error("API error:", err);
      setResponse("Error occurred");
    }
  };

  return (
    <>
      <div className="d-flex justify-content-center align-items-center vh-100 gap-3 bg-dark p-3">
        <div className="card bg-secondary text-light h-75" style={{ width: '700px' }}>
          <div className="card-body">
            {/* Title to ask the user for a question */}
            <h2 className="text-center mb-4">Ask a Question</h2>
            <form onSubmit={(e) => {e.preventDefault(); handleSubmit(question);}}>
              <div className="input-group mb-3">
                {/* input prompt */}
                <input
                  type="text"
                  className="form-control"
                  placeholder="Type your question..."
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                />
                {/* submit button */}
                <button className="btn btn-primary" type="submit">
                  Submit
                </button>
              </div>
            </form>
            
            {/* if given response, give answer */}
            {response && (
              <div className='d-flex align-items-start gap-3 mt-4'>
                {/* add my profile image */}
                <img 
                  src={Profile} 
                  alt="Profile" 
                  className="rounded-circle flex-shrink-0" 
                  style={{ width: '60px', height: '60px', objectFit: 'cover' }}
                />
                {/* add an alert with the response */}
                <div className='flex-grow-1'>
                  <div className="alert alert-info m-0" role="alert">
                    {response}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  )
}

export default App
