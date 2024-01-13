// Import the createClient function from the Supabase JavaScript client library
//import { createClient } from '@supabase/supabase-js';

// Initialize the Supabase client
const database = supabase.createClient('https://nzwdhyxjyncysjamcjzz.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im56d2RoeXhqeW5jeXNqYW1janp6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDUxMjkzMjgsImV4cCI6MjAyMDcwNTMyOH0.J4xwhdheALeSQ2LYCPV_2UMu8TPd2XAiaClskaybwdc');

async function submitJobForm() {
    // Get form values
    const companyName = document.getElementById('companyName').value;
    const jobTitle = document.getElementById('jobTitle').value;
    const deadline = document.getElementById('deadline').value;
    const jobDescriptionFile = document.getElementById('jobDescription').files[0];
    const csvFile = document.getElementById('csvFile').files[0];

    // Validate form values (add additional validation as needed)
    if (!companyName || !jobTitle || !deadline || !jobDescriptionFile || !csvFile) {
        alert("Please fill out all fields.");
        return;
    }

    // Read the content of the job description file
    const jobDescriptionContent = await readFileAsync(jobDescriptionFile);

    // Read the content of the CSV file
    const csvContent = await readFileAsync(csvFile);

    // Convert CSV content to an array of skills (customize this based on your CSV structure)
    const skillsArray = csvContent.split(',');


    let res = await database.from("recruiter_table").insert({
        company_name: companyName,
        job_title: jobTitle,
        deadline: deadline,
        job_description: jobDescriptionContent,
        skills: skillsArray
    })

    if (res) {
        console.log('Job information submitted successfully:');
        alert('Job information submitted successfully!');
    } else {
        console.error('Error inserting data into Supabase:');
        alert('Error submitting job information. Please try again.');
    }
}

function readFileAsync(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = (event) => resolve(event.target.result);
        reader.onerror = (error) => reject(error);
        reader.readAsText(file);
    });
}
