async function getdata() {
    const response = await fetch('/data')
    const data = await response.json()
    const semesters = data.data
    const selectElement = document.getElementById('semseter')

    // Clear existing options
    selectElement.innerHTML = '<option value="0" selected>Pilih Semester</option>'

    // Populate the select dropdown with semester options
    semesters.forEach(semester => {
        const option = document.createElement('option')
        option.value = semester.semester
        option.textContent = `Semester ${semester.semester}`
        selectElement.appendChild(option)
    })
}

async function semseter() {
    var semseter = document.getElementById("semseter").value
    var option = document.getElementById("konsentrasi-option")
    if (Number(semseter) >= 3) {
        option.disabled = false
    } else {
        option.disabled = true
    }
}

async function populateCourseInputs() {
    const response = await fetch('/data')
    const data = await response.json()
    const semesterSelect = document.getElementById('semseter')
    const courseInputsDiv = document.getElementById('courseInputs')
    const consentrationOption = document.getElementById("konsentrasi-option").value
    
    // Clear existing input fields
    courseInputsDiv.innerHTML = ''

    // Find selected semester
    const selectedSemester = semesterSelect.value

    // Find data for selected semester
    const selectedSemesterData = data.data.find(semester => semester.semester === selectedSemester)

    // If semester data is found, create input fields for each course
    if (selectedSemesterData) {
        
        if (Number(selectedSemester) >= 3 && Number(selectedSemester) <=5) {
            if (consentrationOption == "0") {
                // If no data found for selected konsentrasi, display a message
                const message = document.createElement('p')
                message.textContent = 'Pilih konsentrasi untuk mengisi nilai'
                courseInputsDiv.appendChild(message)
            } else {
                // Find data for consentration

                selectedSemesterData.data.forEach(course => {
                    if (course.name == "Konsentrasi") {
                        // Check if selectedSemesterData is found
                        if (selectedSemesterData) {
                            // Find the object with the key "Konsentrasi"
                            const konsentrasiObject = selectedSemesterData.data.find(item => item.name === 'Konsentrasi');
                            // If konsentrasi object is found, push its data to the konsentrasiData array
                            if (konsentrasiObject) {
                                const consentrationData = konsentrasiObject.data.find(item => item.konsentrasi === consentrationOption)
                                consentrationData.data.forEach(course => { 
                                    const courseId = course.name.replace(/\s+/g, '_'); // Replace spaces with underscore
                                    // Create label for course name
                                    const courseLabel = document.createElement('label')
                                    courseLabel.setAttribute('for', courseId)
                                    courseLabel.textContent = `${course.name} (${course.sks})`
                
                                    // Create input field for entering grade
                                    const gradeInput = document.createElement('input')
                                    gradeInput.setAttribute('type', 'text')
                                    gradeInput.setAttribute('class', 'form-control')
                                    gradeInput.setAttribute('id', courseId)
                                    gradeInput.setAttribute('name', courseId)
                                    gradeInput.setAttribute('placeholder', 'Enter grade')
                
                                    // Create div to contain label and input field
                                    const courseDiv = document.createElement('div')
                                    courseDiv.setAttribute('class', 'mb-3')
                                    courseDiv.appendChild(courseLabel)
                                    courseDiv.appendChild(gradeInput)
                
                                    // Append course div to the container
                                    courseInputsDiv.appendChild(courseDiv)
                                })
                            }
                        }
                    } else {
                        const courseId = course.name.replace(/\s+/g, '_'); // Replace spaces with underscore
                        // Create label for course name
                        const courseLabel = document.createElement('label')
                        courseLabel.setAttribute('for', courseId)
                        courseLabel.textContent = `${course.name} (${course.sks})`
    
                        // Create input field for entering grade
                        const gradeInput = document.createElement('input')
                        gradeInput.setAttribute('type', 'text')
                        gradeInput.setAttribute('class', 'form-control')
                        gradeInput.setAttribute('id', courseId)
                        gradeInput.setAttribute('name', courseId)
                        gradeInput.setAttribute('placeholder', 'Enter grade')
    
                        // Create div to contain label and input field
                        const courseDiv = document.createElement('div')
                        courseDiv.setAttribute('class', 'mb-3')
                        courseDiv.appendChild(courseLabel)
                        courseDiv.appendChild(gradeInput)
    
                        // Append course div to the container
                        courseInputsDiv.appendChild(courseDiv)
                    }
                })
            }
        } else {
            selectedSemesterData.data.forEach(course => {
                const courseId = course.name.replace(/\s+/g, '_'); // Replace spaces with underscore
                const courseLabel = document.createElement('label')
                courseLabel.setAttribute('for', courseId)
                courseLabel.textContent = `${course.name} (${course.sks})`
    
                const courseInput = document.createElement('input')
                courseInput.setAttribute('type', 'text')
                courseInput.setAttribute('class', 'form-control')
                courseInput.setAttribute('id', courseId)
                courseInput.setAttribute('name', courseId)
    
                const courseDiv = document.createElement('div')
                courseDiv.setAttribute('class', 'mb-3')
                courseDiv.appendChild(courseLabel)
                courseDiv.appendChild(courseInput)
    
                courseInputsDiv.appendChild(courseDiv)
            })
        }
    } else {
        // If no data found for selected semester, display a message
        const message = document.createElement('p')
        message.textContent = 'Pilih semester untuk mengisi nilai'
        courseInputsDiv.appendChild(message)
    }
}

function autoFormatNIM(input) {
  var value = input.value;
  var originalLength = value.length;
  var caretPosition = input.selectionStart;

  value = value.replace(/[^0-9]/g, ''); // Hapus semua karakter non-angka
  var parts = [];

  // Bagi string menjadi bagian 23.83.1040
  if (value.length > 2) {
    parts.push(value.substring(0, 2));
    if (value.length > 4) {
      parts.push(value.substring(2, 4));
      if (value.length > 8) {
        parts.push(value.substring(4, 8));
      } else {
        parts.push(value.substring(4));
      }
    } else {
      parts.push(value.substring(2));
    }
  } else {
    parts.push(value);
  }

  // Gabungkan bagian dengan titik
  input.value = parts.join('.');

  // Atur kembali posisi kursor
  if (originalLength < input.value.length) {
    caretPosition++;
  }
  input.setSelectionRange(caretPosition, caretPosition);
}

// Call the function to populate course inputs when the semester select is changed
document.getElementById('semseter').addEventListener('change', populateCourseInputs)

// Populate course inputs on page load
populateCourseInputs()
semseter()
getdata()
formatnim()
