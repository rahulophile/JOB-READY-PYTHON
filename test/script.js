// --- PARSED QUIZ DATA ---
// Maine tumhare text ko parse karke yeh structure banaya hai.
// Har question ek object hai jisme 'question', 'options', aur 'correctAnswers' (index based) hain.
// 'source' batata hai ki question Swayam ka hai ya Official Solution ka.

const quizData = [
    // --- Questions from Swayam Interface Screenshots ---
    // Week 0
    {
        source: "Swayam Interface",
        week: 0,
        question: "Which software is usually used for network access control in an organizational network?",
        options: [
            "Firewall",
            "Gateway",
            "Router",
            "Virus checker"
        ],
        correctAnswers: [0] // index of 'Firewall'
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "Which of the following is/are used for connectionless sockets?",
        options: [
            "Datagram Socket only",
            "Datagram Packet only",
            "Both (i) and (ii)",
            "None of these"
        ],
        correctAnswers: [2] // index of 'Both (i) and (ii)'
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "Which of the following is most appropriate about Threads? Threads of a process share",
        options: [
            "only global variables.",
            "only heap.",
            "neither global variables nor heap.",
            "both heap and global variables."
        ],
        correctAnswers: [3]
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "What is the maximum number of hosts under class B addresses?",
        options: [
            "65536",
            "65534",
            "65535",
            "254"
        ],
        correctAnswers: [1]
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "Consider a system with 2 level caches. The access times of Level 1 cache, Level 2 cache, and main memory are 1 ns, 10ns, and 400 ns, respectively. The hit rates of Level 1 and Level 2 caches are 0.8 and 0.9, respectively. What is the average access time of the system, ignoring the search time within the cache?",
        options: [
            "12.6 ns",
            "11.2 ns",
            "10.6 ns",
            "12.4 ns"
        ],
        correctAnswers: [2]
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "Using a larger block size in a fixed block size file system leads to",
        options: [
            "better disk throughput but poorer disk space utilization",
            "better disk throughput and better disk space utilization",
            "poorer disk throughput but better disk space utilization",
            "poorer disk throughput and poorer disk space utilization"
        ],
        correctAnswers: [0]
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "Transport layer is implemented in the NIC of a typical computer system.",
        options: [
            "True",
            "False"
        ],
        correctAnswers: [1]
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "A computer's processor sends 32 bit addresses to the cache controller. It has a 512 KByte, 8-way set associative, write back data cache with block size of 32 Bytes. In addition to the address tag, each cache tag directory entry contains 3 valid bits and 1 modified bit. Find the size of the cache tag directory.",
        options: [
            "212 Kbits",
            "160 Kbits", // Assuming this is correct based on user checkmark
            "320 Kbits",
            "120 Kbits"
        ],
        correctAnswers: [1]
    },
     {
        source: "Swayam Interface",
        week: 0,
        question: "Flow control is mainly implemented in",
        options: [
            "Physical Layer",
            "Application Layer",
            "Transport Layer",
            "Session Layer"
        ],
        correctAnswers: [2]
    },
    {
        source: "Swayam Interface",
        week: 0,
        question: "Where does the swap space reside?",
        options: [
            "RAM",
            "Disk",
            "ROM",
            "On-chip cache"
        ],
        correctAnswers: [1]
    },
    // Week 1 - Swayam
    {
        source: "Swayam Interface",
        week: 1,
        question: "Which of the following fall(s) under the \"essential characteristics\" of cloud computing?",
        options: [
            "A. Resource Pooling",
            "B. Measured Service",
            "C. Rapid Elasticity",
            "D. Latency"
        ],
        correctAnswers: [0, 1, 2] // Multiple correct
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "\"Google Slide\" is an example of",
        options: [
            "a. PaaS",
            "b. IaaS",
            "c. SaaS",
            "d. FaaS"
        ],
        correctAnswers: [2]
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "Which of the following is/are public cloud platform(s)?",
        options: [
            "a. Windows Server Hyper-V",
            "b. Google Cloud Interconnect",
            "c. Amazon Virtual Private Cloud",
            "d. Microsoft Azure"
        ],
        correctAnswers: [3]
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "VM technology allows multiple virtual machines to run on a single physical system.",
        options: [
            "a. True",
            "b. False"
        ],
        correctAnswers: [0]
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "Which one of the following is/are disadvantage(s) of cloud computing?",
        options: [
            "a. Resource pooling",
            "b. It requires an always-on internet connection.",
            "c. Ubiquitous",
            "d. On-demand payment policy"
        ],
        correctAnswers: [1]
    },
     {
        source: "Swayam Interface",
        week: 1,
        question: "For less data-intensive applications, horizontal scale-out elasticity is the ideal solution.",
        options: [
            "a. True",
            "b. False"
        ],
        correctAnswers: [1]
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "The combination of Service-Oriented Infrastructure and Cloud Computing realizes to ______",
        options: [
            "a. FTP",
            "b. SNTP",
            "c. XaaS",
            "d. FaaS"
        ],
        correctAnswers: [2]
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "What is/are the main requirement(s) of a Cloud Service Provider (CSP)?",
        options: [
            "a. Increase agility",
            "b. Increase cost",
            "c. Increase productivity",
            "d. Decrease cost"
        ],
        correctAnswers: [0, 2] // Multiple correct
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "PaaS (Platform as a Service) brings the benefits: (i) Creation of software (ii) Integration of web services and databases",
        options: [
            "a. Only (i)",
            "b. Only (ii)",
            "c. Both (i) and (ii)",
            "d. Neither (i) nor (ii)"
        ],
        correctAnswers: [2]
    },
    {
        source: "Swayam Interface",
        week: 1,
        question: "A ______ is a distributed computer system that consists of a collection of interconnected stand-alone computers working together as an integrated computing resource.",
        options: [
            "a. Grid",
            "b. Cluster",
            "c. Cloud",
            "d. Node"
        ],
        correctAnswers: [1]
    },
    // Week 2 - Swayam
    {
        source: "Swayam Interface",
        week: 2,
        question: "The public cloud has a risk of multi-tenancy.",
        options: [
            "A. True",
            "B. False"
        ],
        correctAnswers: [0]
    },
    {
        source: "Swayam Interface",
        week: 2,
        question: "Ubuntu Enterprise Cloud (UEC) is an example of",
        options: [
            "A. Private cloud",
            "B. Public cloud",
            "C. Hybrid cloud",
            "D. Community Cloud"
        ],
        correctAnswers: [0]
    },
    {
        source: "Swayam Interface",
        week: 2,
        question: "Organization should consider-(i) Network Dependency and (ii) Risks from multi-tenancy while thinking of deploying an outsourced private cloud.",
        options: [
            "A. Only (i)",
            "B. Only (ii)",
            "C. Both (i) and (ii)",
            "D. None of (i) and (ii)"
        ],
        correctAnswers: [2]
    },
     {
        source: "Swayam Interface",
        week: 2,
        question: "Which of the following is/are XML parser API(s)?",
        options: [
            "A. XaaS (Anything as a Model)",
            "B. DOM (Document Object Model)",
            "C. CLI (Command Line Interface)",
            "D. SLA (Service Level Agreement)"
        ],
        correctAnswers: [1] // Only DOM was checked
    },
    {
        source: "Swayam Interface",
        week: 2,
        question: "What is/are the main difference(s) between virtualization and dual boot?",
        options: [
            "A. No difference between dual boot and virtualization.",
            "B. In virtualization, operating systems are not isolated from each other, but not in dual boot.",
            "C. In a dual boot, both operating systems run simultaneously, but not in virtualization.",
            "D. In virtualization, both operating systems run simultaneously, but not in dual boot."
        ],
        correctAnswers: [3]
    },
    {
        source: "Swayam Interface",
        week: 2,
        question: "In virtualization, a virtual machine monitor is also called",
        options: [
            "A. Hypervisor",
            "B. Short-term Scheduler",
            "C. Analyzer",
            "D. Parser"
        ],
        correctAnswers: [0]
    },
     {
        source: "Swayam Interface",
        week: 2,
        question: "Speed and flexibility are the two disadvantages of hardware-assisted virtualization.",
        options: [
            "A. True",
            "B. False"
        ],
        correctAnswers: [0] // Marked as True in Swayam screenshot
    },
    {
        source: "Swayam Interface",
        week: 2,
        question: "The following problems are addressed through Web services:",
        options: [
            "A. Firewall",
            "B. Interoperability",
            "C. Complexity",
            "D. Speed"
        ],
        correctAnswers: [0, 1, 2] // Multiple checked
    },
    {
        source: "Swayam Interface",
        week: 2,
        question: "A web service can be discovered using",
        options: [
            "A. SMS",
            "B. HTTP",
            "C. SMTP",
            "D. UDDI"
        ],
        correctAnswers: [3]
    },
     {
        source: "Swayam Interface",
        week: 2,
        question: "Service-Oriented Architecture (SOA) consists of relationships between:",
        options: [
            "A. Two entities ( a service provider and a requestor)",
            "B. Two entities ( a service provider and a broker)",
            "C. Three entities ( a service provider, a service requestor, and a broker)",
            "D. Three entities ( a service provider, a service requestor, and a hypervisor)"
        ],
        correctAnswers: [2]
    },

    // --- Add Weeks 3 to 12 from Swayam Interface similarly ---
    // --- Example: Week 12, Q10 ---
     {
        source: "Swayam Interface",
        week: 12,
        question: "5G network technology has proven to offer a theoretical download speed of 1Gbit/s.",
        options: [
            "a. True",
            "b. False"
        ],
        correctAnswers: [1] // 'b' was selected in Swayam
    },

    // --- Questions from Official NPTEL Solution Pages ---
    // Week 1 - Official
    {
        source: "Official Solution",
        week: 1,
        question: "Which of the following fall(s) under the “essential characteristics” of cloud computing?",
        options: [
            "A. Resource Pooling",
            "B. Measured Service",
            "C. Rapid Elasticity",
            "D. Latency"
        ],
        correctAnswers: [0, 1, 2]
    },
    {
        source: "Official Solution",
        week: 1,
        question: "\"Google Doc\" is an example of",
        options: [
            "A. PaaS",
            "B. IaaS",
            "C. SaaS",
            "D. FaaS"
        ],
        correctAnswers: [2]
    },
     {
        source: "Official Solution",
        week: 1,
        question: "Business-Process-as-a-Service is not a part of XaaS.",
        options: [
            "A) True",
            "B) False"
        ],
        correctAnswers: [1]
    },
    {
        source: "Official Solution",
        week: 1,
        question: "Network Function Virtualization involves the implementation of __________ function in software that can run on a range of industry-standard servers __________.",
        options: [
            "A. network,software",
            "B. hardware, software",
            "C. hardware, network",
            "D. network,hardware"
        ],
        correctAnswers: [3]
    },
    {
        source: "Official Solution",
        week: 1,
        question: "Which are the following applications for SaaS (Software as a Service) architecture?",
        options: [
            "A) Billing software",
            "B) CRM",
            "C) App engines",
            "D) None of above"
        ],
        correctAnswers: [0, 1]
    },
     {
        source: "Official Solution",
        week: 1,
        question: "Web access to commercial software is one of the SaaS characteristics in the cloud computing paradigm.",
        options: [
            "A. True",
            "B. False"
        ],
        correctAnswers: [0]
    },
    {
        source: "Official Solution",
        week: 1,
        question: "In the case of the client-server model: Statement (i) Virtualization is a core concept; Statement (ii) system can scale infinitely",
        options: [
            "A) Only Statement (i) is correct",
            "B) Only Statement (ii) is correct",
            "C) Both Statements (i) and (ii) are correct",
            "D) None of the statements is correct"
        ],
        correctAnswers: [3]
    },
    {
        source: "Official Solution",
        week: 1,
        question: "Client-server model is always load-balanced",
        options: [
            "A) True",
            "B) False"
        ],
        correctAnswers: [1]
    },
     {
        source: "Official Solution",
        week: 1,
        question: "PaaS (Platform as a Service) brings the benefits: (i) Creation of software (ii) Integration of web services and databases",
        options: [
            "A. Only (i)",
            "B. Only (ii)",
            "C. Both (i) and (ii)",
            "D. Neither (i) nor (ii)"
        ],
        correctAnswers: [2]
    },
    {
        source: "Official Solution",
        week: 1,
        question: "Which of the following is false?",
        options: [
            "a) Private cloud is dedicated solely to an organization.",
            "b) Community cloud is a composition of public and private cloud.",
            "c) Public cloud is available to the general public.",
            "d) None of these"
        ],
        correctAnswers: [1]
    },
    // --- Add Weeks 2, 5, 6, 7, 8, 9, 10, 11, 12 from Official Solutions similarly ---
    // --- Example: Week 12, Q10 - Official ---
     {
        source: "Official Solution",
        week: 12,
        question: "What is(are) the benefit(s) of 5G technology for enhanced mobile broadband?",
        options: [
            "A) Slower data rates",
            "B) Higher latency",
            "C) Lower cost-per-bit",
            "D) Limited device compatibility"
        ],
        correctAnswers: [2] // Index of 'C'
    },

];
// --- END OF DATA ---

// DOM Elements
const questionHeaderEl = document.getElementById('question-header');
const questionNumberEl = document.getElementById('question-number');
const totalQuestionsEl = document.getElementById('total-questions');
const questionTextEl = document.getElementById('question-text');
const optionsContainerEl = document.getElementById('options-container');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const feedbackEl = document.getElementById('feedback');
const sourceIndicatorEl = document.getElementById('source-indicator');


// State
let currentQuestionIndex = 0;
let answerSelected = false; // To prevent multiple selections per question

// --- Functions ---

function loadQuestion() {
    answerSelected = false; // Reset selection flag
    feedbackEl.textContent = ''; // Clear previous feedback
    const currentQuestion = quizData[currentQuestionIndex];

    questionNumberEl.textContent = currentQuestionIndex + 1;
    totalQuestionsEl.textContent = quizData.length;
    questionTextEl.textContent = currentQuestion.question;
    sourceIndicatorEl.textContent = `Source: ${currentQuestion.source} - Week ${currentQuestion.week}`;


    optionsContainerEl.innerHTML = ''; // Clear previous options

    currentQuestion.options.forEach((optionText, index) => {
        const optionElement = document.createElement('div');
        optionElement.classList.add('option');
        // Remove ✓ or ✅ if present for display, keep original index association
        optionElement.textContent = optionText.replace(/^[✓✅]\s*/, '');
        optionElement.dataset.index = index; // Store the original index

        optionElement.addEventListener('click', () => selectAnswer(optionElement, index));
        optionsContainerEl.appendChild(optionElement);
    });

    // Update button states
    prevBtn.disabled = currentQuestionIndex === 0;
    nextBtn.disabled = currentQuestionIndex === quizData.length - 1;

     // Scroll question text back to top
    questionTextEl.scrollTop = 0;
}

function selectAnswer(selectedOptionElement, selectedIndex) {
    if (answerSelected) return; // Prevent selecting again
    answerSelected = true;

    const currentQuestion = quizData[currentQuestionIndex];
    const correctAnswersIndices = currentQuestion.correctAnswers; // Array of correct indices
    const isCorrect = correctAnswersIndices.includes(selectedIndex);

    // Disable all options after selection
    const allOptionElements = optionsContainerEl.querySelectorAll('.option');
    allOptionElements.forEach(el => el.classList.add('disabled')); // Add disabled class


    if (isCorrect) {
        selectedOptionElement.classList.add('correct');
        feedbackEl.textContent = "Correct!";
        feedbackEl.style.color = "green";
        // Also highlight other correct answers if it's a multiple-correct question
        correctAnswersIndices.forEach(correctIndex => {
            if (correctIndex !== selectedIndex) {
                 const correctEl = optionsContainerEl.querySelector(`.option[data-index='${correctIndex}']`);
                 if(correctEl) correctEl.classList.add('correct');
            }
        });
    } else {
        selectedOptionElement.classList.add('incorrect');
        feedbackEl.textContent = "Incorrect!";
        feedbackEl.style.color = "red";
        // Highlight all correct answers in green
        correctAnswersIndices.forEach(correctIndex => {
            const correctEl = optionsContainerEl.querySelector(`.option[data-index='${correctIndex}']`);
            if(correctEl) correctEl.classList.add('correct');
        });
    }
}

function nextQuestion() {
    if (currentQuestionIndex < quizData.length - 1) {
        currentQuestionIndex++;
        loadQuestion();
    }
}

function prevQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        loadQuestion();
    }
}

// --- Event Listeners ---
prevBtn.addEventListener('click', prevQuestion);
nextBtn.addEventListener('click', nextQuestion);

// --- Initial Load ---
loadQuestion();