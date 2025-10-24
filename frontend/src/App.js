import React, { useEffect, useState } from 'react';
import axios from 'axios';
import BuildList from './components/BuildList';

function App(){
  const [jobs, setJobs] = useState([]);

  useEffect(()=>{
    axios.get('/api/jenkins/jobs').then(res=>{
      setJobs(res.data.jobs || []);
    }).catch(err=>{
      console.error(err);
    })
  },[]);

  return (
    <div style={{padding:20}}>
      <h2>Smart CI Monitor - Dashboard</h2>
      <BuildList jobs={jobs} />
    </div>
  )
}

export default App;
