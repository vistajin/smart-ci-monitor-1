import React from 'react';

function BuildList({jobs}){
  if(!jobs || jobs.length===0) return <div>No jobs found (backend may be down)</div>;
  return (
    <div>
      {jobs.map(job=>(
        <div key={job.name} style={{border:'1px solid #ddd', padding:10, marginBottom:8}}>
          <div><strong>{job.name}</strong></div>
          <div>Last Build: {job.last_build ? job.last_build.number : 'N/A'} - {job.last_build ? job.last_build.result : ''}</div>
        </div>
      ))}
    </div>
  )
}

export default BuildList;
