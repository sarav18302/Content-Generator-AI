import React, { useState } from 'react'
import "../App.css";
import axios from 'axios';
export const HomePage = () => {
    
    const [data, setData] = useState("");
    const [pred,setPred] = useState("");
    const handleButtonClick = async() =>{
      try {
        const response = await axios.post("http://127.0.0.1:5000", {
            prompt: data
        });
  
        console.log(response.data.predict)
        setPred(response.data.predict);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  return (
    <>
    <div className='textarea-container'>

<textarea id="Text1" cols="50" rows="22" value={data} onChange={e =>setData(e.target.value)} />



  <input type = "button" value="Generate text" className="button1" onClick={()=>handleButtonClick()}/>

</div>
<div className="output">{pred}</div>
    </>
    
  )
}
