async function getdata() {
    const response = await fetch('/data');
    const data = await response.json();
    const semesters = data.data;
    const selectElement = document.getElementById('konsentrasi');

    // Clear existing options
    selectElement.innerHTML = '<option value="0" selected>Pilih Semester</option>';

    // Populate the select dropdown with semester options
    semesters.forEach(semester => {
        const option = document.createElement('option');
        option.value = semester.semester;
        option.textContent = `Semester ${semester.semester}`;
        selectElement.appendChild(option);
    });
}

async function populateCourseInputs() {
    const response = await fetch('/data');
    const data = await response.json();
    const semesterSelect = document.getElementById('konsentrasi');
    const courseInputsDiv = document.getElementById('courseInputs');
    
    // Clear existing input fields
    courseInputsDiv.innerHTML = '';

    // Find selected semester
    const selectedSemester = semesterSelect.value;

    // Find data for selected semester
    const selectedSemesterData = data.data.find(semester => semester.semester === selectedSemester);

    // If semester data is found, create input fields for each course
    if (selectedSemesterData) {
        selectedSemesterData.data.forEach(course => {
            const courseLabel = document.createElement('label');
            const courseId = course.name.replace(/\s+/g, '_'); // Replace spaces with underscore
            courseLabel.setAttribute('for', courseId);
            courseLabel.textContent = `${course.name} (${course.sks})`;

            const courseInput = document.createElement('input');
            courseInput.setAttribute('type', 'text');
            courseInput.setAttribute('class', 'form-control');
            courseInput.setAttribute('id', courseId); // Set ID without spaces

            const courseDiv = document.createElement('div');
            courseDiv.setAttribute('class', 'mb-3');
            courseDiv.appendChild(courseLabel);
            courseDiv.appendChild(courseInput);

            courseInputsDiv.appendChild(courseDiv);
        });
    } else {
        // If no data found for selected semester, display a message
        const message = document.createElement('p');
        message.textContent = 'No courses found for selected semester';
        courseInputsDiv.appendChild(message);
    }
}

// Call the function to populate course inputs when the semester select is changed
document.getElementById('konsentrasi').addEventListener('change', populateCourseInputs);

// Populate course inputs on page load
populateCourseInputs();


// Call the function to populate course inputs when the semester select is changed
document.getElementById('konsentrasi').addEventListener('change', populateCourseInputs);


function konsentrasi() {
    var konsentrasi = document.getElementById("konsentrasi").value
    var option = document.getElementById("konsentrasi-option")
    if (Number(konsentrasi) > 2) {
        option.disabled = false
    } else {
        option.disabled = true
    }
}

getdata()
// Populate course inputs on page load
populateCourseInputs();