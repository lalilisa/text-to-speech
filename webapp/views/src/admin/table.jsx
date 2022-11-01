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
                <div className='logout'>
                    <span className="user">Trí Mai</span> <button className="logoutbutton">Log out</button>
                </div>
        <div className="container-table100" style={{width:'100%',padding:0,margin:0}}>
           <div className="wrap-table100" style={{width:'100%',padding:0,margin:0}}>
              <div className="table100 ver2 m-b-110">
                 <div className="table100-head">
                    <table style={{width:'100%'}}>
                       <thead>
                          <tr className="row100 head">
                             <th className="cell100 column1" >ID</th>
                             <th className="cell100 column2">Input</th>
                             <th className="cell100 column3">Output</th>
                             <th className="cell100 column4">Words</th>
                             <th className="cell100 column5">Audio path</th>
                             <th className="cell100 column6">Hash code</th>
                             <th className="cell100 column7">Action</th>
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
                                           <td className="cell100 column2"style={{textAlign:'center',wordWrap:'break-word'}}>{value.inputText}</td>
                                           <td className="cell100 column3" style={{textAlign:'center',wordWrap:'break-word'}}>{value.audioNameOutput}</td>
                                           <td className="cell100 column4" style={{textAlign:'center',wordWrap:'break-word'}}>{value.words}</td>
                                           <td className="cell100 column5" style={{textAlign:'center',wordWrap:'break-word'}}>{value.outputPathAudio}</td>
                                           <td className="cell100 column6" style={{textAlign:'center',wordWrap:'break-word'}}>{value.hashcode}</td>
                                           <td className="cell100 column7"><button className="btn-delete">Delete</button></td>
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