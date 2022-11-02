import '../admin/css/tables/animate.css'
import '../admin/css/tables/bootstrap.min.css'
import '../admin/css/tables/font-awesome.min.css'
import '../admin/css/tables/main.css'
import '../admin/css/tables/util.css'
import '../admin/css/tables/perfect-scrollbar.css'
import '../admin/css/tables/select2.min.css'
import '../admin/css/tables/logoutbutton.css'
import { useEffect, useState } from 'react'
import axios from 'axios'
export const Table=()=>{

    const [data, setData] = useState([]);

    useEffect( () => {
        const fetchData= async ()=>{
           const result= await axios.get('http://localhost/audio')
           const datas= await result.data;
           setData(datas);
        
        }
        fetchData()
      });
 
    return(
      <div className="limiter" style={{width:'100%',margin:0,position:"relative",top:'0',backgroundColor:'white'}}>
	  
      <div className="container-table100">
      <div className="btn-place">
         <div className="upload-btn">
            <input type="file" id="fileID" style={{display:'none'}}/>
            <label tabindex="0" for="fileID" className="btn-up">Upload a file</label>
         </div>
         <div className="train-btn">
            <button className="btn-train">Train model</button>
         </div>	
      </div>
         <div className="wrap-table100">
            <div className="table100 ver2 m-b-110">
               <div className="table100-head">
                  <table>
                     <thead>
                        <tr className="row100 head">
                           <th className="cell100 column1">ID</th>
                           <th className="cell100 column2">Input</th>
                           <th className="cell100 column3">Words</th>
                    <th className="cell100 column4">Audio path</th>
                    <th className="cell100 column5">Action</th>
                        </tr>
                     </thead>
                  </table>
               </div>
               <div className="table100-body js-pscroll ps ps--active-y">
                  <table>
                     <tbody>
                     {data.map((value)=>
                        <tr className="row100 body">
                           <td className="cell100 column1">{value.id}</td>
                           <td className="cell100 column2">{value.inputText}</td>
                           <td className="cell100 column3">{value.words}</td>
                           <td className="cell100 column4">{value.outputPathAudio}</td>
                           <td className="cell100 column5">
                              <button className="btn-delete">Edit</button>
                              <button className="btn-delete" onClick={()=>{ axios.delete(`http://localhost/audio/${value.id}`).then(response=>{
                                                                                                                           console.log(response)
                                                                                                                        })
                                                                                                                        .catch(err=>{
                                                                                                                           console.log(err)
                                                                                                                        }) }} >Delete</button>
                           </td>
                        </tr>
                        )}
                     </tbody>
                  </table>

               </div>

            </div>

          
               </div>
            </div>
         </div>

    )
}