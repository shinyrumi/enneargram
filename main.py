import streamlit as st
import streamlit.components.v1 as components # components.html을 사용하기 위해 import

st.title("enneargram") # 'enneagram'이 아닐까요? :)
st.write("Hello, 에니어그램 테스트에 오신 것을 환영합니다!") # 간단한 안내 문구 추가

# 제공해주신 HTML, CSS, JavaScript 코드를 하나의 큰 문자열로 만듭니다.
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>에니어그램 자가 진단 테스트 by @peace_shiny</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Noto Sans KR', 'Inter', sans-serif;
            background-color: #FFF0F5; /* LavenderBlush */
            overscroll-behavior-y: contain; 
        }
        #test-container {
            background-color: #ffffff;
            border-radius: 20px; 
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08), 0 6px 15px rgba(0, 0, 0, 0.06); 
            border: 1px solid #FFDDEE; 
        }
        #test-container h1 {
            font-family: 'Gaegu', cursive; 
            color: #C71585; /* MediumVioletRed */
            font-size: 2.5rem; 
        }
        #step-indicator {
            color: #DB7093; /* PaleVioletRed */
            font-weight: 700;
        }
        #step-title {
            font-family: 'Gaegu', cursive;
            color: #C71585; 
            font-size: 1.8rem;
        }
        #instruction {
            color: #555; 
            font-size: 1rem;
        }

        .question-group {
            margin-bottom: 2rem;
            padding: 1.5rem; 
            border: 1px dashed #FFB6C1; 
            border-radius: 15px; 
            background-color: #fffafa; 
        }
        .question-group h3 {
            font-family: 'Gaegu', cursive;
            font-size: 1.5rem; 
            font-weight: 700; 
            color: #CD5C5C; /* IndianRed */
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 2px dotted #FFC0CB; 
        }
        .question-item {
            padding: 1.2rem;
            border: 1px solid #fce4ec; 
            border-radius: 12px;
            margin-bottom: 1rem;
            background-color: #ffffff; 
            box-shadow: 0 3px 6px rgba(255, 182, 193, 0.2); 
        }
        .question-item p {
            color: #4a5568; 
            line-height: 1.7; 
            font-size: 0.95rem;
        }
        .rating-options label {
            margin-right: 0.5rem;
            padding: 0.7rem 1.1rem; 
            border: 1px solid #FFDDEE; 
            border-radius: 20px; 
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 500;
            transition: background-color 0.2s, border-color 0.2s, color 0.2s, transform 0.1s;
            color: #C71585; 
            background-color: #fff0f5; 
            display: inline-block; 
        }
        .rating-options input[type="radio"]:checked + label {
            background-color: #FF69B4; /* HotPink */
            color: white;
            border-color: #FF1493; /* DeepPink */
            transform: scale(1.05); 
        }
        .rating-options input[type="radio"] + label:hover {
            background-color: #ffe4e1; /* MistyRose */
            border-color: #ffc0cb; /* Pink */
        }
        .rating-options input[type="radio"] { 
            opacity: 0;
            position: fixed;
            width: 0;
        }
        .rating-options input[type="radio"]:focus-visible + label { 
            box-shadow: 0 0 0 2px #FF69B4;
        }
        
        .button-container {
            display: flex;
            justify-content: space-between;
            margin-top: 1.5rem;
        }

        #prev-button, #next-button, #restart-button {
            padding: 0.875rem 1.5rem; 
            font-size: 1.1rem;
            font-weight: 700;
            border-radius: 25px; 
            box-shadow: 0 5px 10px rgba(0,0,0,0.1);
            transition: background-color 0.2s, transform 0.1s;
            font-family: 'Gaegu', cursive;
            cursor: pointer;
        }
        #prev-button {
            background-color: #FFDEAD; /* NavajoWhite */
            color: #8B4513; /* SaddleBrown */
            border: 2px solid #FFA07A; /* LightSalmon */
        }
        #prev-button:hover {
            background-color: #FFA07A; /* LightSalmon */
            color: white;
        }
        #next-button {
            background-color: #FF69B4; /* HotPink */
            color: white;
            border: 2px solid #FF1493;
        }
        #next-button:hover {
            background-color: #FF1493; /* DeepPink */
        }
        #restart-button {
            background-color: #90EE90; /* LightGreen */
            color: #2F4F4F; /* DarkSlateGray */
            border: 2px solid #3CB371; /* MediumSeaGreen */
            width: 100%; /* Restart button full width */
        }
        #restart-button:hover {
            background-color: #3CB371; /* MediumSeaGreen */
            color: white;
        }
        #prev-button:hover, #next-button:hover, #restart-button:hover {
            transform: translateY(-2px) scale(1.02); 
        }


        #result-area {
            border: 2px dashed #FFB6C1; 
            border-radius: 15px;
        }
        #result-area h2 {
            font-family: 'Gaegu', cursive;
            color: #C71585;
            font-size: 2rem;
        }
        .result-section {
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 12px;
            border-width: 1px;
        }
        .result-section h3 {
            font-family: 'Gaegu', cursive;
            font-size: 1.4rem; 
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        .result-section p {
            font-size: 1rem; 
            line-height: 1.7;
            color: #555;
        }
        .result-section.bg-blue-50 { background-color: #E0FFFF; border-color: #AFEEEE; } 
        .result-section.bg-blue-50 h3 { color: #5F9EA0; } 
        .result-section.bg-green-50 { background-color: #F0FFF0; border-color: #98FB98; } 
        .result-section.bg-green-50 h3 { color: #2E8B57; } 
        .result-section.bg-yellow-50 { background-color: #FFFACD; border-color: #FAFAD2; } 
        .result-section.bg-yellow-50 h3 { color: #FF8C00; } 

        #error-message {
            font-family: 'Gaegu', cursive;
            font-size: 1.1rem;
            color: #DC143C; /* Crimson */
        }
        footer {
            font-family: 'Gaegu', cursive;
            text-align: center;
            font-size: 0.9rem;
            color: #DB7093; /* PaleVioletRed */
            margin-top: 2.5rem;
            padding-top: 1rem;
            border-top: 1px dotted #FFC0CB; /* Pink */
        }
        footer span {
            font-weight: 700;
            color: #C71585; /* MediumVioletRed */
        }

        /* 모바일 환경 최적화 */
        @media (max-width: 768px) {
            #test-container h1 { font-size: 2rem; }
            #step-title { font-size: 1.5rem; }
            .question-group h3 { font-size: 1.3rem; }
            .question-item p { font-size: 0.9rem; }
            .rating-options label { padding: 0.6rem 0.9rem; font-size: 0.85rem; }
            .rating-options { justify-content: space-evenly; }
            #options-area { max-height: 65vh; } /* 오타 수정: max-h-[65vh] -> max-height: 65vh */
            #prev-button, #next-button, #restart-button { font-size: 1rem; }
            .result-section h3 { font-size: 1.2rem; }
            .result-section p { font-size: 0.9rem; }
            .button-container { flex-direction: column; gap: 0.5rem; }
            #prev-button, #next-button { width: 100%; }
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
    <div id="test-container" class="bg-white p-6 md:p-10 rounded-lg shadow-xl w-full max-w-3xl">
        <h1 class="text-3xl md:text-4xl font-bold text-center text-gray-800 mb-8">💖 에니어그램 자가 진단 💖</h1>
        
        <div id="step-indicator" class="text-center text-sm text-blue-700 font-semibold mb-6"></div>
        <div id="question-title-area" class="mb-6">
            <h2 id="step-title" class="text-2xl font-semibold text-gray-700 mb-3"></h2>
            <p id="instruction" class="text-md text-gray-600 leading-relaxed"></p>
        </div>

        <div id="options-area" class="space-y-4 mb-6 max-h-[60vh] overflow-y-auto pr-2 pb-2">
        </div>
        
        <div class="button-container">
            <button id="prev-button" class="hidden">⏪ 이전</button>
            <button id="next-button">다음 🚀</button>
        </div>

        <div id="error-message" class="text-red-600 text-sm mt-3 text-center hidden font-medium">
            모든 항목에 답변해주세요.
        </div>

        <div id="result-area" class="mt-10 p-6 bg-gray-50 rounded-lg shadow-inner hidden">
            <h2 class="text-2xl md:text-3xl font-semibold text-gray-800 mb-6 text-center">🌟 당신의 에니어그램 분석 결과 🌟</h2>
            <div id="result-content" class="space-y-4 text-gray-700">
            </div>
            <button id="restart-button" class="mt-8">다시 시작! 🌱</button>
        </div>
        <footer>
            Lovingly Crafted by <span>@peace_shiny</span> 💖✨
        </footer>
    </div>

    <script>
        const enneagramData = {
            centers: [ 
                { 
                    id: "heart", 
                    name: "가슴형 (감정 중심)", 
                    description: "주로 감정을 통해 세상을 경험하고 소통합니다. 타인과의 관계, 인정, 그리고 자신의 정체성에 깊은 관심을 가집니다. 이들은 다른 사람들과의 연결을 중요하게 생각하며, 사랑받고 인정받으려는 욕구가 강합니다. 때로는 자신의 감정이나 타인의 감정에 쉽게 휩싸일 수 있으며, 수치심은 이 중심의 주요 감정적 주제입니다. 가슴형은 타인에게 어떻게 비치는지, 그리고 관계 속에서 자신의 가치를 찾으려는 경향이 두드러집니다.", 
                    types: [2, 3, 4] 
                },
                { 
                    id: "head", 
                    name: "머리형 (사고 중심)", 
                    description: "주로 사고와 분석을 통해 세상을 이해하려고 합니다. 안전, 정보, 그리고 미래에 대한 계획에 중점을 둡니다. 이들은 불확실성을 줄이고 예측 가능성을 높이려 하며, 지식과 논리를 중요하게 여깁니다. 두려움은 이 중심의 주요 감정적 주제이며, 이를 다루는 방식이 다양하게 나타납니다. 머리형은 안전을 확보하고 미래의 위험에 대비하기 위해 정신적인 전략을 사용하는 경향이 있습니다.", 
                    types: [5, 6, 7] 
                },
                { 
                    id: "gut", 
                    name: "장형 (본능 중심)", 
                    description: "주로 본능과 직관에 따라 행동하며, 자신의 의지와 힘을 중요하게 생각합니다. 환경에 대한 통제, 자율성, 그리고 정의에 대한 욕구가 강합니다. 이들은 현실에 직접적으로 관여하고 자신의 존재감을 드러내려 하며, 분노는 이 중심의 주요 감정적 주제입니다. 장형은 자신의 공간을 지키고 현실에 영향을 미치려는 본능적인 힘을 중요시합니다.", 
                    types: [8, 9, 1] 
                }
            ],
            centerIdentificationGroups: [
                { 
                    groupId: "groupA", 
                    groupName: "A 그룹 질문", 
                    questions: [
                        { text: "나는 다른 사람들의 감정 변화를 잘 알아채는 편이다.", id: "ci_A_1", centerTarget: "heart" },
                        { text: "다른 사람들에게 인정받고 좋은 관계를 맺는 것이 나에게 중요하다.", id: "ci_A_2", centerTarget: "heart" },
                        { text: "나의 이미지가 다른 사람들에게 어떻게 보일지 신경 쓰는 편이다.", id: "ci_A_3", centerTarget: "heart" },
                        { text: "나는 다른 사람의 기분을 맞추려고 노력할 때가 많다.", id: "ci_A_4", centerTarget: "heart" },
                        { text: "나는 내가 특별하거나 독특한 사람이라고 느끼고 싶어 한다.", id: "ci_A_5", centerTarget: "heart" }
                    ]
                },
                { 
                    groupId: "groupB", 
                    groupName: "B 그룹 질문",
                    questions: [
                        { text: "나는 어떤 일을 결정하기 전에 정보를 충분히 수집하고 분석하는 것을 선호한다.", id: "ci_B_1", centerTarget: "head" },
                        { text: "미래에 발생할 수 있는 문제나 위험에 대해 미리 생각하고 대비하는 경향이 있다.", id: "ci_B_2", centerTarget: "head" },
                        { text: "새로운 아이디어나 다양한 가능성을 탐색하는 것을 즐긴다.", id: "ci_B_3", centerTarget: "head" },
                        { text: "나는 어떤 상황에서든 안전하다고 느끼는 것이 매우 중요하다.", id: "ci_B_4", centerTarget: "head" },
                        { text: "나는 종종 최악의 시나리오를 상상하며 미리 걱정하는 편이다.", id: "ci_B_5", centerTarget: "head" }
                    ]
                },
                { 
                    groupId: "groupC", 
                    groupName: "C 그룹 질문",
                    questions: [
                        { text: "나는 내가 옳다고 생각하는 것을 주장하고 상황을 주도하려는 경향이 있다.", id: "ci_C_1", centerTarget: "gut" },
                        { text: "불편하거나 부당하다고 느끼는 상황에 대해 직접적으로 반응하는 편이다.", id: "ci_C_2", centerTarget: "gut" },
                        { text: "나는 내 주변 환경이나 상황이 내 뜻대로 통제되기를 바란다.", id: "ci_C_3", centerTarget: "gut" },
                        { text: "나는 갈등 상황을 피하기보다는 정면으로 맞서는 것을 선호한다.", id: "ci_C_4", centerTarget: "gut" },
                        { text: "나는 나의 직감이나 본능에 따라 행동할 때가 많다.", id: "ci_C_5", centerTarget: "gut" }
                    ]
                }
            ],
            types: { 
                1: { 
                    name: "1번: 개혁가", 
                    description: "원칙을 중시하고 세상을 더 나은 곳으로 만들고자 하는 강한 욕구를 가집니다. 자신과 타인에게 높은 기준을 적용하며, 옳고 그름에 대한 명확한 신념을 가지고 있습니다. 책임감이 강하고 성실하지만, 때로는 지나치게 비판적이거나 융통성이 부족해 보일 수 있습니다. 내면의 '비평가' 목소리에 따라 완벽을 추구하며, 분노를 억제하려는 경향이 있습니다. 이들은 종종 자신의 이상과 현실 사이의 괴리감으로 인해 내적 긴장을 경험하며, 자기 개선과 주변 환경 개선에 끊임없이 노력합니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "자신의 건강, 안전, 재정적 안정 등 개인적인 안녕과 환경의 완벽함에 주로 관심을 둡니다. 미리 계획하고 대비함으로써 불안을 관리하려 하며, 세부 사항에 매우 꼼꼼합니다. 종종 걱정이 많고 자신에게 엄격하며, 자원 관리와 질서 유지를 중요하게 생각합니다. 이들은 '완벽한 준비'를 통해 미래의 위험으로부터 자신을 보호하려 하며, 종종 사소한 것에도 신경을 많이 쓰는 경향이 있습니다.",
                            questions: [
                                { text: "나는 나의 건강이나 안전, 재정적 안정에 대해 자주 걱정하고, 만일의 사태에 대비하려고 한다.", id: "st_1_sp_1" },
                                { text: "나는 내 주변 환경(집, 작업 공간 등)이 깔끔하고 질서정연하게 유지되기를 바란다.", id: "st_1_sp_2" },
                                { text: "나는 규칙을 잘 지키고, 계획에 따라 일이 진행되는 것을 선호한다.", id: "st_1_sp_3" },
                                { text: "나는 사소한 실수나 결점에도 민감하게 반응하며, 이를 바로잡으려고 한다.", id: "st_1_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "가까운 관계나 자신이 중요하다고 생각하는 대상을 '개선'하고 완벽하게 만들려는 강한 열정을 보입니다. 이상적인 관계나 파트너에 대한 기준이 매우 높으며, 옳고 그름에 대한 자신의 신념을 관계 속에서 강하게 표현합니다. 때로는 비판적이거나 요구가 많은 모습으로 비칠 수 있으며, 질투심이나 강렬한 감정을 경험할 수 있습니다. 이들은 관계 속에서 '완벽한 연결'을 추구하며, 상대방에게도 높은 수준의 도덕성과 헌신을 기대합니다.",
                            questions: [
                                { text: "나는 내가 중요하다고 생각하는 사람이나 대상을 더 완벽하게 만들고 싶은 강한 열정을 느낀다.", id: "st_1_sx_1" },
                                { text: "나는 관계에서 '옳음'과 '정의'를 강하게 추구하며, 상대방도 이를 따르기를 기대한다.", id: "st_1_sx_2" },
                                { text: "나는 파트너나 가까운 사람이 나의 높은 기준에 부응하지 못할 때 실망하거나 비판적이 된다.", id: "st_1_sx_3" },
                                { text: "나는 관계에서 강렬한 감정적 교류와 이상적인 모습을 중요하게 생각한다.", id: "st_1_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "사회적으로 올바르고 모범적인 사람이 되려고 노력하며, 집단이나 사회의 규칙과 기준을 개선하여 더 나은 공동체를 만들고자 합니다. 객관성과 공정성을 강조하며, 종종 교육자나 지도자의 역할을 합니다. 다른 1번 유형에 비해 덜 비판적으로 보일 수 있으며, 사회적 책임감이 강하고 '올바른 역할 모델'이 되려고 합니다. 이들은 '완벽한 사회'를 만드는 데 기여하고자 하며, 이를 위해 적극적으로 참여하고 목소리를 냅니다.",
                            questions: [
                                { text: "나는 사회적으로 올바른 모범을 보이고, 더 나은 사회를 만들기 위해 노력하는 것을 중요하게 생각한다.", id: "st_1_so_1" },
                                { text: "나는 집단이나 조직 내에서 공정하고 합리적인 규칙과 시스템이 잘 작동하는 것에 관심이 많다.", id: "st_1_so_2" },
                                { text: "나는 다른 사람들에게 올바른 길을 제시하고, 그들이 더 나은 방향으로 나아가도록 돕고 싶다.", id: "st_1_so_3" },
                                { text: "나는 사회적 문제나 불의에 대해 목소리를 내고, 이를 개선하기 위한 활동에 참여하는 것을 중요하게 여긴다.", id: "st_1_so_4" }
                            ]
                        }
                    }
                },
                2: { 
                    name: "2번: 조력가", 
                    description: "타인의 필요에 민감하게 반응하며, 따뜻함과 친절함으로 다른 사람을 돕고자 하는 강한 욕구를 가집니다. 관계를 매우 중요하게 생각하며, 사랑받고 인정받기 위해 노력합니다. 공감 능력이 뛰어나지만, 때로는 자신의 필요를 간과하고 타인에게 지나치게 관여하거나 소유욕을 보일 수 있습니다. 거절에 민감하고 칭찬과 감사에 큰 의미를 둡니다. 이들은 타인과의 연결을 통해 자신의 가치를 확인하려는 경향이 있으며, 종종 '나는 필요한 사람인가?'라는 질문을 스스로에게 던집니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "다른 2번 유형보다 자신의 필요에 더 초점을 맞추며, 도움을 주고받는 관계에서 자신이 특별한 대우를 받기를 기대할 수 있습니다. 매력적이고 아이 같은 순수함으로 타인의 보호 본능을 자극하여 도움을 얻으려 하며, 독립과 의존 사이에서 갈등할 수 있습니다. '나는 보살핌 받을 자격이 있어'라는 무의식적 믿음이 있으며, 자신의 안락함과 안전을 중요시합니다. 이들은 도움을 통해 자신의 안전을 확보하려는 경향이 있습니다.",
                            questions: [
                                { text: "나는 다른 사람들에게 도움을 줄 때, 그들이 나를 특별하게 여기고 나에게 필요한 것을 제공해주기를 기대한다.", id: "st_2_sp_1" },
                                { text: "나는 때때로 어린아이처럼 다른 사람의 보살핌과 관심을 받고 싶어 한다.", id: "st_2_sp_2" },
                                { text: "나는 나의 편안함과 안정을 위해 다른 사람의 도움이 필요하다고 느낄 때가 있다.", id: "st_2_sp_3" },
                                { text: "나는 내가 베푼 만큼 상대방도 나에게 관심을 가져주기를 바란다.", id: "st_2_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "특정 개인과의 강렬하고 친밀한 관계를 추구하며, 자신의 매력을 적극적으로 사용하여 상대방을 유혹하고 사로잡으려 합니다. 상대방에게 깊은 영향을 미치고, 없어서는 안 될 존재가 되기를 원합니다. 감정적으로 매우 열정적이고 헌신적이지만, 때로는 소유욕이 강하게 나타나거나 관계에 집착하는 모습을 보일 수 있습니다. 이들은 한 사람에게 집중하여 '운명적인 사랑'을 꿈꾸며, 그 관계가 자신의 전부인 것처럼 행동할 수 있습니다.",
                            questions: [
                                { text: "나는 특정 사람과의 관계에서 매우 강렬한 감정적 연결과 친밀감을 추구한다.", id: "st_2_sx_1" },
                                { text: "나는 나의 매력을 사용하여 상대방을 사로잡고, 그 사람에게 가장 중요한 존재가 되기를 원한다.", id: "st_2_sx_2" },
                                { text: "나는 사랑하는 사람에게 모든 것을 주고 싶어 하며, 그 사람의 전부가 되고 싶어 한다.", id: "st_2_sx_3" },
                                { text: "나는 관계에서 상대방의 관심과 애정을 독점하고 싶어 하는 경향이 있다.", id: "st_2_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "넓은 사회적 관계망 속에서 중요한 인물이 되고자 하는 야망을 가집니다. 다른 사람들을 돕고 지원함으로써 집단 내에서 영향력을 행사하고 인정을 받으려 합니다. 사교적이고 활동적이며, 모임이나 그룹을 이끄는 역할을 즐겨 합니다. '나는 많은 사람들에게 필요한 존재가 될 것이다'라는 동기가 강하며, 때로는 자신의 이미지를 위해 과도하게 노력할 수 있습니다. 이들은 '집단의 중심'이 되기를 원하며, 이를 통해 자신의 가치를 확인받고자 합니다.",
                            questions: [
                                { text: "나는 넓은 사회적 관계망 속에서 다른 사람들에게 영향력을 미치고 인정받는 것을 중요하게 생각한다.", id: "st_2_so_1" },
                                { text: "나는 여러 사람을 돕고 지원함으로써 집단 내에서 중요한 역할을 하고 싶어 한다.", id: "st_2_so_2" },
                                { text: "나는 다른 사람들을 연결해주고 모임을 주도하는 것을 즐긴다.", id: "st_2_so_3" },
                                { text: "나는 많은 사람들로부터 좋은 평판을 얻고, 그들에게 필요한 사람으로 인식되기를 바란다.", id: "st_2_so_4" }
                            ]
                        }
                    }
                },
                3: { 
                    name: "3번: 성취가", 
                    description: "성공과 성취를 통해 자신의 가치를 증명하고 타인에게 인정받고자 하는 강한 동기를 가집니다. 매우 활동적이고 경쟁심이 강하며, 효율성과 생산성을 중시합니다. 자신의 이미지에 신경을 많이 쓰며, 능력 있고 성공적인 모습으로 보이기를 원합니다. 상황에 맞춰 자신을 잘 적응시키지만, 진정한 감정을 드러내는 데 어려움을 겪을 수 있습니다. 실패를 두려워하며, 끊임없이 다음 목표를 향해 나아갑니다. 이들은 '나는 내가 하는 일이다'라는 믿음을 가질 수 있습니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "성공과 성취를 통해 물질적인 안정과 안전을 확보하는 데 중점을 둡니다. 매우 열심히 일하고 효율성을 극대화하여 실질적인 결과를 얻으려고 합니다. 자신의 능력과 자원을 관리하는 데 능숙하며, 낭비를 싫어합니다. 겉으로 드러나는 화려함보다는 실질적인 부와 안정을 추구하는 경향이 있습니다. 이들은 '자수성가'하여 안전한 기반을 마련하는 것을 중요시하며, 이를 위해 끊임없이 노력합니다.",
                            questions: [
                                { text: "나는 나의 능력과 노력을 통해 물질적인 안정과 안전을 확보하는 것을 매우 중요하게 생각한다.", id: "st_3_sp_1" },
                                { text: "나는 일을 효율적으로 처리하고 실질적인 성과를 내는 데 집중하며, 낭비를 싫어한다.", id: "st_3_sp_2" },
                                { text: "나는 성공을 통해 다른 사람에게 의존하지 않고 자립할 수 있는 능력을 갖추기를 원한다.", id: "st_3_sp_3" },
                                { text: "나는 나의 성과가 구체적인 물질적 보상으로 이어지는 것을 중요하게 생각한다.", id: "st_3_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "다른 사람, 특히 이성이나 중요한 대상에게 매력적이고 이상적인 모습으로 보이기를 원합니다. 자신의 외모, 재능, 성격 등을 가꾸어 타인의 시선을 사로잡고 긍정적인 반응을 얻으려고 합니다. 관계에서의 성공을 중요하게 생각하며, 인기 있고 주목받는 역할을 즐깁니다. 때로는 진정한 자신보다 만들어진 이미지에 더 집중할 수 있습니다. 이들은 '가장 매력적인 파트너'가 되거나 그런 파트너를 얻는 것을 중요시하며, 이를 위해 자신을 적극적으로 어필합니다.",
                            questions: [
                                { text: "나는 다른 사람들, 특히 내가 중요하게 생각하는 사람들에게 매력적이고 이상적인 모습으로 보이기를 원한다.", id: "st_3_sx_1" },
                                { text: "나는 관계에서 성공하고, 상대방에게 깊은 인상을 남기며 주목받는 것을 즐긴다.", id: "st_3_sx_2" },
                                { text: "나는 나의 외모나 스타일, 재능 등을 통해 다른 사람들의 관심과 칭찬을 받고 싶어 한다.", id: "st_3_sx_3" },
                                { text: "나는 파트너에게 최고의 모습만을 보여주려고 노력하며, 관계가 성공적으로 보이도록 신경 쓴다.", id: "st_3_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "사회적으로 인정받고 존경받는 지위나 역할을 얻기 위해 노력합니다. 자신의 성과를 통해 집단이나 사회에 기여하고, 이를 통해 명예와 인정을 얻고자 합니다. 리더십을 발휘하고, 성공적인 롤모델로서 타인에게 영감을 주기를 원합니다. 자신의 이미지가 사회적으로 어떻게 비치는지 매우 중요하게 생각하며, 실패나 부정적인 평가를 두려워합니다. 이들은 '사회적 성공의 아이콘'이 되기를 꿈꾸며, 이를 통해 자신의 가치를 세상에 증명하고자 합니다.",
                            questions: [
                                { text: "나는 사회적으로 높은 지위를 얻거나 명성을 쌓아 많은 사람들에게 인정받고 존경받기를 원한다.", id: "st_3_so_1" },
                                { text: "나는 성공적인 역할 모델이 되어 다른 사람들에게 영감을 주고, 사회에 긍정적인 영향을 미치고 싶다.", id: "st_3_so_2" },
                                { text: "나는 나의 성과나 업적이 공개적으로 인정받고 칭찬받는 것을 중요하게 생각한다.", id: "st_3_so_3" },
                                { text: "나는 다른 사람들이 나를 어떻게 평가하는지에 대해 매우 민감하며, 좋은 이미지를 유지하려고 노력한다.", id: "st_3_so_4" }
                            ]
                        }
                    }
                },
                4: { 
                    name: "4번: 개인주의자", 
                    description: "자신을 독특하고 특별한 존재로 여기며, 평범함을 거부합니다. 감수성이 풍부하고 예민하며, 감정의 깊이를 중요하게 생각합니다. 창의적이고 예술적인 성향을 가지고 있으며, 아름다움을 추구합니다. 자신의 내면세계에 깊이 몰두하며, 때로는 우울감이나 고독감을 느끼기 쉽습니다. 타인과의 깊은 정서적 교감을 갈망하며, 자신을 진정으로 이해해주는 사람을 찾습니다. 이들은 종종 '결핍감'을 느끼며, 이상적인 것을 갈망하고, 자신만의 독특한 세계를 구축하려 합니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "자신의 감정적인 고통이나 어려움을 밖으로 드러내기보다는 내면에서 묵묵히 견디려는 성향을 보입니다. 때로는 위험을 감수하거나 극단적인 경험을 통해 자신의 강인함을 시험하기도 합니다. 낭만적인 면모보다는 현실적인 어려움 속에서 자신만의 의미를 찾으려는 모습이 나타날 수 있습니다. 타인에게 의존하기보다는 스스로 해결하려는 자립심이 강하며, 겉으로는 무덤덤해 보일 수 있습니다. 이들은 '고통을 견디는 강인한 개인'이라는 이미지를 통해 자신의 특별함을 유지하려 할 수 있습니다.",
                            questions: [
                                { text: "나는 감정적인 고통이나 어려움을 겪을 때, 이를 밖으로 드러내기보다는 혼자 묵묵히 견디는 편이다.", id: "st_4_sp_1" },
                                { text: "나는 때때로 위험을 감수하거나 극단적인 경험을 통해 나 자신의 한계를 시험하고 싶어 한다.", id: "st_4_sp_2" },
                                { text: "나는 다른 사람에게 의존하기보다는 스스로의 힘으로 어려움을 극복하려는 경향이 있다.", id: "st_4_sp_3" },
                                { text: "나는 나의 내면적인 강인함을 중요하게 생각하며, 감정에 휘둘리지 않으려고 노력한다.", id: "st_4_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "감정을 매우 강렬하게 경험하고 표현하며, 특히 관계에서 질투, 분노, 실망 등의 감정을 격렬하게 느낄 수 있습니다. 타인과의 관계에서 특별하고 깊은 연결을 갈망하지만, 동시에 상대방이 자신의 기대를 충족시키지 못할 때 크게 실망하고 비난하는 경향이 있습니다. 경쟁심이 강하게 나타날 수 있으며, '특별한 나를 몰라주는' 세상이나 타인에 대한 분노를 표출하기도 합니다. 이들은 '격정적인 관계'를 통해 자신의 존재감을 확인하려 하며, 드라마틱한 감정의 기복을 경험할 수 있습니다.",
                            questions: [
                                { text: "나는 관계에서 매우 강렬한 감정을 경험하며, 질투나 분노, 실망 같은 감정을 격렬하게 느끼고 표현하는 편이다.", id: "st_4_sx_1" },
                                { text: "나는 특별하고 깊은 관계를 갈망하지만, 상대방이 나의 기대를 충족시키지 못하면 크게 실망하고 비판적으로 변하기도 한다.", id: "st_4_sx_2" },
                                { text: "나는 다른 사람이 가진 것을 부러워하거나, 그들과 경쟁하려는 마음이 들 때가 있다.", id: "st_4_sx_3" },
                                { text: "나는 나의 감정을 솔직하고 강렬하게 표현하는 것이 진실된 관계라고 생각한다.", id: "st_4_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "사회적인 상황에서 자신이 남들과 다르거나 부족하다고 느끼며 수치심을 경험하기 쉽습니다. 자신의 독특함을 유지하려 하지만 동시에 사회에 소속되고 인정받고 싶은 욕구 사이에서 갈등합니다. 자신의 감정과 경험을 진솔하게 표현하려 하며, 피상적인 관계보다는 깊이 있는 소통을 원합니다. 타인의 고통에 민감하게 공감하며, 사회적 약자나 소외된 존재에 대해 연민을 느낍니다. 이들은 '이해받는 특별함'을 추구하며, 자신의 다름이 인정받기를 바랍니다.",
                            questions: [
                                { text: "나는 종종 사회적인 상황에서 내가 남들과 다르거나 부족하다고 느껴 수치심을 경험한다.", id: "st_4_so_1" },
                                { text: "나는 피상적인 관계보다는 나의 진솔한 감정과 생각을 나눌 수 있는 깊이 있는 소통을 중요하게 생각한다.", id: "st_4_so_2" },
                                { text: "나는 다른 사람들의 고통에 깊이 공감하며, 소외된 존재에 대해 특별한 연민을 느낀다.", id: "st_4_so_3" },
                                { text: "나는 나의 독특함이 다른 사람들에게 이해받고 받아들여지기를 바란다.", id: "st_4_so_4" }
                            ]
                        }
                    }
                },
                5: { 
                    name: "5번: 탐구가", 
                    description: "지식과 정보를 수집하고 분석하는 것을 통해 세상을 이해하려고 합니다. 객관적이고 논리적이며, 감정 표현에 서툴거나 거리를 두는 경향이 있습니다. 독립적이며, 자신만의 시간과 공간을 매우 중요하게 생각합니다. 에너지와 자원을 아끼려는 경향이 있으며, 타인에게 의존하는 것을 꺼립니다. 관찰력이 뛰어나고 통찰력이 있지만, 사회적인 상호작용보다는 내면의 세계에 머무르는 것을 선호할 수 있습니다. 이들은 '유능한 전문가'가 되기를 원하며, 세상의 복잡함을 이해하려는 지적 욕구가 강합니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "자신의 시간, 에너지, 공간 등 자원을 철저하게 관리하고 보호하려는 욕구가 강합니다. 외부 세계로부터 자신을 차단하고 안전한 '요새'와 같은 개인적인 공간에서 지내는 것을 선호합니다. 타인과의 교류를 최소화하며, 혼자만의 시간을 통해 지식을 탐구하고 에너지를 충전합니다. 이들은 '침해받지 않는 독립성'을 최우선으로 하며, 자신의 경계를 철저히 지킵니다.",
                            questions: [
                                { text: "나는 나만의 시간과 공간, 그리고 에너지를 매우 중요하게 생각하며, 이것이 침해받는 것을 극도로 싫어한다.", id: "st_5_sp_1" },
                                { text: "나는 외부의 방해 없이 안전한 나만의 공간에서 지식을 탐구하고 생각을 정리하는 것을 선호한다.", id: "st_5_sp_2" },
                                { text: "나는 다른 사람들과의 불필요한 교류를 피하고, 혼자 있는 시간을 통해 에너지를 충전한다.", id: "st_5_sp_3" },
                                { text: "나는 나의 자원을 아끼고 효율적으로 사용하는 것을 중요하게 생각한다.", id: "st_5_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "소수의 특별한 사람과 깊고 신뢰할 수 있는 관계를 맺기를 원합니다. 자신의 내면세계나 비밀스러운 생각, 지식을 공유할 수 있는 상대를 찾습니다. 관계에서 강렬한 지적, 정서적 교감을 추구하며, 일단 신뢰하는 상대에게는 매우 헌신적일 수 있습니다. 하지만 관계가 침해당하거나 기대에 미치지 못하면 깊은 상처를 받고 철회할 수 있습니다. 이들은 '완벽한 이해자'와의 깊은 연결을 갈망하며, 그 관계 안에서만 자신의 진정한 모습을 드러낼 수 있습니다.",
                            questions: [
                                { text: "나는 소수의 특별한 사람과 깊고 신뢰할 수 있는 관계를 맺어, 나의 내면세계나 비밀스러운 지식을 공유하고 싶다.", id: "st_5_sx_1" },
                                { text: "나는 관계에서 강렬한 지적, 정서적 교감을 추구하며, 일단 신뢰하는 상대에게는 매우 헌신적이다.", id: "st_5_sx_2" },
                                { text: "나는 상대방과 모든 것을 공유하고 완벽하게 이해받는 이상적인 관계를 꿈꾼다.", id: "st_5_sx_3" },
                                { text: "나는 신뢰하는 소수의 사람 외에는 나의 사적인 생각이나 감정을 잘 드러내지 않는다.", id: "st_5_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "자신이 가진 지식이나 전문성을 통해 사회나 집단에 기여하고자 합니다. 특정 분야의 전문가가 되어 자신의 지혜와 통찰력을 다른 사람들과 공유하는 데 가치를 둡니다. 이상적인 사회나 시스템에 대한 관심이 많으며, 이를 분석하고 비전을 제시할 수 있습니다. 직접적인 사회 활동보다는 자신의 지식을 통해 간접적으로 영향을 미치는 것을 선호할 수 있습니다. 이들은 '지혜로운 현자'로서의 역할을 추구하며, 자신의 지식이 세상에 유용하게 쓰이기를 바랍니다.",
                            questions: [
                                { text: "나는 내가 가진 전문 지식이나 통찰력을 통해 사회나 특정 집단에 기여하고 싶다.", id: "st_5_so_1" },
                                { text: "나는 이상적인 사회나 시스템에 대해 깊이 생각하며, 나의 지혜를 다른 사람들과 공유하는 데 가치를 둔다.", id: "st_5_so_2" },
                                { text: "나는 특정 분야의 전문가가 되어 다른 사람들에게 인정받고, 나의 지식으로 영향을 미치고 싶다.", id: "st_5_so_3" },
                                { text: "나는 복잡한 문제에 대해 깊이 분석하고, 객관적인 해결책이나 비전을 제시하는 것을 중요하게 생각한다.", id: "st_5_so_4" }
                            ]
                        }
                    }
                },
                6: { 
                    name: "6번: 충성가", 
                    description: "안전을 추구하며, 잠재적인 위험과 위협에 대해 민감하게 반응합니다. 책임감이 강하고 성실하며, 자신이 속한 공동체나 신념에 충실합니다. 의심이 많고 불안감을 느끼기 쉬우며, 최악의 상황을 미리 대비하려고 합니다. 권위에 대해 복종적이거나 혹은 반항적인 양면성을 보일 수 있으며, 신뢰할 수 있는 지지 기반을 찾는 것이 중요합니다. 이들은 '안전한 세상'을 갈망하며, 끊임없이 주변을 경계하고 신뢰할 대상을 찾습니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "안전과 안정을 확보하기 위해 주변 사람들과 따뜻하고 우호적인 관계를 맺으려고 노력합니다. 불안감을 많이 느끼며, 이를 해소하기 위해 신뢰할 수 있는 사람이나 시스템에 의존하려는 경향이 있습니다. 위험을 피하고 신중하게 행동하며, 자신을 보호해 줄 수 있는 동맹을 중요하게 생각합니다. 이들은 '안전한 울타리' 안에서 평화를 찾으려 하며, 개인적인 관계를 통해 안정감을 얻습니다.",
                            questions: [
                                { text: "나는 안전과 안정을 확보하기 위해 주변 사람들과 따뜻하고 우호적인 관계를 맺으려고 노력한다.", id: "st_6_sp_1" },
                                { text: "나는 잠재적인 위험에 대해 미리 걱정하고, 신뢰할 수 있는 사람이나 시스템에 의존하여 불안감을 해소하려 한다.", id: "st_6_sp_2" },
                                { text: "나는 위험을 감수하기보다는 신중하게 행동하며, 나를 지켜줄 수 있는 사람들과 함께 있는 것을 선호한다.", id: "st_6_sp_3" },
                                { text: "나는 다른 사람들과의 약속이나 합의를 중요하게 생각하며, 이를 통해 안정감을 느낀다.", id: "st_6_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "두려움에 맞서기 위해 힘이나 매력을 추구하거나, 자신을 보호해 줄 수 있는 강한 파트너에게 헌신하는 경향이 있습니다. 관계에서 강렬한 연결과 충성심을 보이지만, 동시에 파트너를 시험하거나 의심할 수도 있습니다. 위협적인 상황에 대담하게 맞서거나(공포 대항형), 반대로 상대방을 이상화하고 맹목적으로 따르는 모습(공포 순응형)을 보일 수 있습니다. 이들은 '강한 보호자' 또는 '매력적인 반항아'의 모습을 통해 자신의 불안을 다룹니다.",
                            questions: [
                                { text: "나는 두려움에 맞서기 위해 나 자신을 강하게 보이려 하거나, 반대로 나를 지켜줄 수 있는 강한 상대에게 헌신한다.", id: "st_6_sx_1" },
                                { text: "나는 관계에서 강렬한 충성심을 보이지만, 때로는 상대방의 진심을 시험하거나 의심하기도 한다.", id: "st_6_sx_2" },
                                { text: "나는 위협적인 상황이나 대상에 대해 대담하게 맞서 싸우려는 용기를 내기도 한다.", id: "st_6_sx_3" },
                                { text: "나는 파트너가 나에게 얼마나 헌신적인지 확인하고 싶어 하며, 관계의 강도를 중요하게 생각한다.", id: "st_6_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "자신이 속한 집단이나 사회의 규칙, 규범, 의무를 중요하게 생각하며 이를 충실히 따르려고 합니다. 권위에 대해 복종적이거나 혹은 회의적인 태도를 보이며, 집단의 안전과 안정을 위해 노력합니다. 공정성과 정의를 중요하게 생각하며, 불확실한 상황에서는 명확한 지침이나 리더를 찾으려고 합니다. 이들은 '신뢰할 수 있는 시스템' 안에서 자신의 역할을 다하고자 하며, 이를 통해 소속감과 안정감을 느낍니다.",
                            questions: [
                                { text: "나는 내가 속한 집단이나 사회의 규칙과 규범을 중요하게 생각하며, 나의 의무를 충실히 이행하려고 한다.", id: "st_6_so_1" },
                                { text: "나는 불확실한 상황에서는 명확한 지침이나 신뢰할 수 있는 권위를 따르는 것을 선호한다.", id: "st_6_so_2" },
                                { text: "나는 공동체의 안전과 안정을 위해 개인적인 희생을 감수할 수 있으며, 집단의 이익을 중요하게 생각한다.", id: "st_6_so_3" },
                                { text: "나는 권위 있는 사람이나 시스템에 대해 의문을 제기하기보다는, 그들이 제시하는 방향을 따르는 편이다.", id: "st_6_so_4" }
                            ]
                        }
                    }
                },
                7: { 
                    name: "7번: 열정가", 
                    description: "즐거움과 새로운 경험을 추구하며, 고통과 제약을 피하려고 합니다. 낙천적이고 활기차며, 다양한 재능과 아이디어를 가지고 있습니다. 호기심이 많고 새로운 것을 배우는 것을 좋아하지만, 깊이 파고들기보다는 여러 가지를 경험하려 합니다. 지루함을 견디기 어려워하며, 미래에 대한 긍정적인 계획을 세우는 것을 좋아합니다. 이들은 '무한한 가능성'을 탐험하는 것을 즐기며, 삶의 밝고 긍정적인 면에 집중하려 합니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "즐거움을 추구하되 좀 더 현실적이고 실질적인 이익을 얻을 수 있는 기회를 포착하는 데 능합니다. 다양한 인맥을 활용하여 자신에게 유리한 상황을 만들고, 안락하고 편안한 환경을 조성하려고 합니다. 다른 7번 유형보다 더 계획적이고 현실 감각이 있을 수 있으며, 물질적인 만족을 중요하게 생각합니다. 이들은 '기회를 놓치지 않는 실속파'이며, 자신의 즐거움을 위해 현실적인 네트워크를 구축합니다.",
                            questions: [
                                { text: "나는 즐거움을 추구하되, 실질적인 이익이나 편안함을 얻을 수 있는 기회를 잘 포착하는 편이다.", id: "st_7_sp_1" },
                                { text: "나는 다양한 인맥을 활용하여 나에게 유리한 상황을 만들고, 안락하고 즐거운 환경을 조성하는 것을 좋아한다.", id: "st_7_sp_2" },
                                { text: "나는 새로운 경험을 할 때, 그것이 나에게 어떤 실질적인 도움이 될지 고려하는 편이다.", id: "st_7_sp_3" },
                                { text: "나는 여러 가지 선택지 중에서 나에게 가장 유리하고 만족스러운 것을 고르는 데 능숙하다.", id: "st_7_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "새로운 경험이나 관계에 대해 강렬한 흥분과 환상을 가집니다. 매력적인 대상이나 아이디어에 쉽게 매료되며, 이를 통해 강렬한 즐거움을 얻으려고 합니다. 상상력이 풍부하고 이상주의적인 면모를 보이며, 현실의 제약보다는 가능성에 초점을 맞춥니다. 때로는 지루함을 피하기 위해 과도하게 자극을 추구하거나 충동적으로 행동할 수 있습니다. 이들은 '매혹적인 이상'에 쉽게 빠져들며, 현실보다는 상상 속의 즐거움을 더 크게 느낄 수 있습니다.",
                            questions: [
                                { text: "나는 새로운 경험이나 아이디어, 매력적인 사람에게 쉽게 매료되며 강렬한 흥분과 환상을 느낀다.", id: "st_7_sx_1" },
                                { text: "나는 지루함을 피하기 위해 끊임없이 새로운 자극을 추구하며, 때로는 충동적으로 행동하기도 한다.", id: "st_7_sx_2" },
                                { text: "나는 현실적인 제약보다는 이상적인 가능성에 더 큰 매력을 느끼며, 그것을 상상하는 것을 즐긴다.", id: "st_7_sx_3" },
                                { text: "나는 내가 매력을 느끼는 대상이나 경험에 대해 쉽게 열광하고 몰입하는 편이다.", id: "st_7_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "집단 전체의 행복과 즐거움을 위해 자신을 희생하거나 봉사하는 모습을 보일 수 있습니다. 이상주의적인 비전을 가지고 있으며, 다른 사람들을 돕고 긍정적인 영향을 미치고 싶어 합니다. 하지만 이 과정에서 자신의 고통이나 부정적인 감정을 회피하려는 경향이 강하게 나타날 수 있습니다. 이들은 '모두를 위한 즐거움'을 추구하지만, 자신의 내면적 어려움은 감추려 하며, 긍정적인 분위기를 유지하는 데 집중합니다.",
                            questions: [
                                { text: "나는 다른 사람들과 함께 즐거움을 나누고, 집단 전체의 행복을 위해 나 자신을 기꺼이 희생하거나 봉사할 수 있다.", id: "st_7_so_1" },
                                { text: "나는 이상적인 비전을 가지고 있으며, 다른 사람들을 돕고 긍정적인 영향을 미치고 싶지만, 그 과정에서 나의 어려움은 잘 드러내지 않는다.", id: "st_7_so_2" },
                                { text: "나는 다른 사람들을 즐겁게 해주고 긍정적인 분위기를 만드는 데 능숙하다.", id: "st_7_so_3" },
                                { text: "나는 개인적인 고통이나 어려움보다는 집단의 즐거움과 긍정적인 면에 집중하려고 한다.", id: "st_7_so_4" }
                            ]
                        }
                    }
                },
                8: { 
                    name: "8번: 도전자", 
                    description: "자신의 힘과 영향력을 중요하게 생각하며, 환경을 통제하려고 합니다. 솔직하고 단호하며, 자신의 주장을 관철시키려는 의지가 강합니다. 정의감이 강하며, 약자를 보호하고 불의에 맞서 싸우려는 경향이 있습니다. 갈등을 두려워하지 않으며, 때로는 공격적이거나 위압적으로 보일 수 있습니다. 자신의 약점을 드러내는 것을 극도로 꺼리며, 타인에게 통제당하는 것을 싫어합니다. 이들은 '강인한 리더'의 모습을 보이며, 자신의 의지대로 세상을 이끌어 가고자 합니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "자신의 생존과 물질적인 필요를 충족시키는 데 매우 직접적이고 단호합니다. 자신의 힘으로 원하는 것을 얻어내며, 타인에게 의존하는 것을 극도로 꺼립니다. 강한 생활력과 현실 감각을 가지고 있으며, 자신의 영역과 소유물을 지키려는 의지가 강합니다. 이들은 '자신의 것을 지키는 생존자'이며, 어떤 상황에서도 살아남고 만족을 얻어내려는 강한 본능을 가집니다.",
                            questions: [
                                { text: "나는 나의 생존과 물질적인 필요를 충족시키는 데 매우 직접적이고 단호하며, 내 힘으로 원하는 것을 얻는다.", id: "st_8_sp_1" },
                                { text: "나는 타인에게 의존하는 것을 싫어하며, 나의 영역과 소유물을 지키려는 의지가 매우 강하다.", id: "st_8_sp_2" },
                                { text: "나는 원하는 것을 얻기 위해 적극적으로 행동하며, 장애물을 극복하는 데 주저함이 없다.", id: "st_8_sp_3" },
                                { text: "나는 나의 자원과 소유물을 통제하고 관리하는 것을 중요하게 생각한다.", id: "st_8_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "관계에서 강한 주도권과 통제력을 행사하려고 하며, 파트너에 대한 강렬한 열정과 소유욕을 보입니다. 카리스마 있고 반항적인 매력을 발산하며, 자신에게 도전하거나 저항하는 상대에게 더 큰 매력을 느낄 수도 있습니다. 옳고 그름보다는 자신의 욕망과 의지를 관철시키는 것을 중요하게 생각합니다. 이들은 '관계를 지배하는 정복자'이며, 강렬한 에너지를 관계에 쏟아붓습니다.",
                            questions: [
                                { text: "나는 관계에서 강한 주도권과 통제력을 행사하려고 하며, 파트너에 대한 강렬한 열정과 소유욕을 보인다.", id: "st_8_sx_1" },
                                { text: "나는 카리스마 있고 반항적인 매력을 발산하며, 나에게 도전하거나 저항하는 상대에게 더 큰 매력을 느낄 수 있다.", id: "st_8_sx_2" },
                                { text: "나는 내가 원하는 것을 얻기 위해 상대방을 설득하거나 압도하는 것을 망설이지 않는다.", id: "st_8_sx_3" },
                                { text: "나는 관계에서 나의 욕망과 의지를 관철시키는 것을 중요하게 생각한다.", id: "st_8_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "사회적 약자나 불의에 맞서 싸우는 데 자신의 힘을 사용합니다. 정의감이 매우 강하며, 자신이 속한 집단이나 동료들을 보호하고 그들과의 연대를 중요하게 생각합니다. 공공연하게 자신의 신념을 주장하며, 부당한 권력에 도전하는 것을 두려워하지 않습니다. 때로는 지나치게 공격적이거나 독선적으로 보일 수 있지만, 그 밑바탕에는 강한 보호 본능과 정의 구현의 욕구가 있습니다. 이들은 '정의를 위한 투사'이며, 공동체를 위해 자신의 힘을 사용합니다.",
                            questions: [
                                { text: "나는 사회적 약자나 불의를 보면 참지 못하고, 나의 힘을 사용하여 그들을 보호하고 정의를 실현하려고 한다.", id: "st_8_so_1" },
                                { text: "나는 내가 속한 집단이나 동료들과의 연대를 중요하게 생각하며, 부당한 권력에 맞서 함께 싸우는 것을 두려워하지 않는다.", id: "st_8_so_2" },
                                { text: "나는 나의 신념을 공공연하게 주장하며, 다른 사람들을 이끌어 공동의 목표를 달성하려고 한다.", id: "st_8_so_3" },
                                { text: "나는 불의에 맞서 싸우고, 내가 옳다고 믿는 것을 위해 기꺼이 대립하는 것을 감수한다.", id: "st_8_so_4" }
                            ]
                        }
                    }
                },
                9: { 
                    name: "9번: 평화주의자", 
                    description: "내면의 평화와 조화를 추구하며, 갈등을 피하려고 합니다. 수용적이고 인내심이 많으며, 타인의 의견을 잘 들어주고 중재하는 역할을 합니다. 느긋하고 편안함을 추구하며, 급격한 변화나 스트레스 상황을 싫어합니다. 자신의 욕구나 의견을 명확하게 표현하기보다는 타인에게 맞추려는 경향이 있습니다. 이들은 '조화로운 안정'을 가장 중요하게 여기며, 이를 위해 자신의 에너지를 분산시키거나 내면으로 숨어들 수 있습니다.",
                    subtypes: {
                        sp: { 
                            name: "SP (자기보존)", 
                            description: "신체적인 편안함과 일상의 안정을 매우 중요하게 생각합니다. 먹고, 자고, 쉬는 등 기본적인 욕구 충족을 통해 평화를 유지하려고 합니다. 변화보다는 익숙하고 예측 가능한 환경을 선호하며, 갈등이나 스트레스를 유발하는 상황을 적극적으로 회피합니다. 중요한 일보다는 당장의 편안함을 주는 사소한 활동에 몰두하며 현실의 문제를 외면할 수 있습니다. 이들은 '일상의 안락함'을 통해 평화를 찾으며, 이를 방해하는 요소를 최소화하려 합니다.",
                            questions: [
                                { text: "나는 신체적인 편안함과 일상의 안정을 매우 중요하게 생각하며, 기본적인 욕구 충족을 통해 평화를 유지하려고 한다.", id: "st_9_sp_1" },
                                { text: "나는 변화보다는 익숙하고 예측 가능한 환경을 선호하며, 갈등이나 스트레스를 유발하는 상황을 적극적으로 회피한다.", id: "st_9_sp_2" },
                                { text: "나는 중요한 일보다는 당장의 편안함을 주는 사소한 활동(TV 시청, 간식 먹기 등)에 몰두하며 시간을 보내는 경향이 있다.", id: "st_9_sp_3" },
                                { text: "나는 갈등이나 불편한 상황을 피하기 위해 나의 욕구나 의견을 억누를 때가 많다.", id: "st_9_sp_4" }
                            ]
                        },
                        sx: { 
                            name: "SX (일대일)", 
                            description: "중요한 타인, 특히 연인이나 배우자와 정서적, 신체적으로 완전히 하나가 되기를 갈망합니다. 상대방의 욕구나 생각에 자신을 맞추고 동화되려는 경향이 강하며, 이를 통해 관계의 평화와 안정을 유지하려고 합니다. 자신의 정체성이나 욕구를 잃어버릴 정도로 상대방에게 몰입할 수 있습니다. 갈등을 피하기 위해 자신의 의견을 거의 내세우지 않습니다. 이들은 '파트너와의 합일'을 통해 평화를 느끼며, 그 관계가 자신의 세계 전부가 될 수 있습니다.",
                            questions: [
                                { text: "나는 중요한 타인, 특히 연인이나 배우자와 정서적, 신체적으로 완전히 하나가 되기를 갈망한다.", id: "st_9_sx_1" },
                                { text: "나는 상대방의 욕구나 생각에 나 자신을 맞추고 동화되려는 경향이 강하며, 이를 통해 관계의 평화를 유지하려고 한다.", id: "st_9_sx_2" },
                                { text: "나는 갈등을 피하기 위해 나의 의견이나 욕구를 표현하기보다는 상대방에게 맞춰주는 편이다.", id: "st_9_sx_3" },
                                { text: "나는 파트너와 함께 있을 때 가장 큰 안정감과 평화를 느끼며, 그 관계에 깊이 몰입한다.", id: "st_9_sx_4" }
                            ]
                        },
                        so: { 
                            name: "SO (사회적)", 
                            description: "자신이 속한 집단이나 공동체의 평화와 조화를 유지하는 데 기여하려고 합니다. 모든 사람의 의견을 존중하고 수용하려고 하며, 갈등 상황에서 중재자 역할을 자처합니다. 소속감을 중요하게 생각하며, 집단 활동에 적극적으로 참여하여 편안함과 안정감을 얻으려고 합니다. 하지만 자신의 진정한 목소리를 내기보다는 집단의 분위기에 휩쓸리기 쉬울 수 있습니다. 이들은 '모두와 함께하는 평화'를 중요시하며, 이를 위해 자신을 드러내기보다 집단에 융화되려 합니다.",
                            questions: [
                                { text: "나는 내가 속한 집단이나 공동체의 평화와 조화를 유지하는 데 기여하려고 하며, 모든 사람의 의견을 존중한다.", id: "st_9_so_1" },
                                { text: "나는 소속감을 중요하게 생각하며, 집단 활동에 적극적으로 참여하여 편안함과 안정감을 얻으려고 한다.", id: "st_9_so_2" },
                                { text: "나는 갈등 상황에서 중재자 역할을 하거나, 모든 사람이 만족할 수 있는 해결책을 찾으려고 노력한다.", id: "st_9_so_3" },
                                { text: "나는 나의 개인적인 의견보다는 집단의 전체적인 분위기나 조화를 더 중요하게 생각하는 경향이 있다.", id: "st_9_so_4" }
                            ]
                        }
                    }
                }
            },
            centerQuestions: { 
                heart: [ 
                    { text: "나는 따뜻하고 친절하다.", type: 2, id: "h_2_1" },
                    { text: "나는 사람들이 나의 조언과 도움을 편안하게 얻기를 바란다.", type: 2, id: "h_2_2" },
                    { text: "받는 것보다 주는 것이 더 편하다.", type: 2, id: "h_2_3" },
                    { text: "나를 무시하거나 내가 한 일에 고마움을 느끼지 않으면 깊이 상처를 받는다.", type: 2, id: "h_2_4" },
                    { text: "반드시 필요한 존재가 되고 싶고 다른 사람들을 더 잘 도울 수 있기를 원한다.", type: 2, id: "h_2_5" },
                    { text: "나는 다른 사람들을 돌봐주느라고 완전히 지쳐버릴 때가 있다.", type: 2, id: "h_2_6" },
                    { text: "나는 존경과 인정, 승인, 찬사를 받는 것을 좋아한다.", type: 2, id: "h_2_7" },
                    { text: "거절하는 것이 어려워 다른사람의 요구를 들어주는 경우가 많다.", type: 2, id: "h_2_8" },
                    { text: "나는 주변사람들을 칭찬해서 내게 특별한 사람이란 것을 알게 하려고 노력한다.", type: 2, id: "h_2_9" },
                    { text: "나는 사람들이 원하는 바를 미리 헤아려서 그렇게 행동하게 된다.", type: 2, id: "h_2_10" },

                    { text: "나는 내 능력에 대해 자신감이 있다.", type: 3, id: "h_3_1" },
                    { text: "내가 이룬 성과에 대해 다른 사람들이 크게 인정을 해줄 때 기분이 좋다.", type: 3, id: "h_3_2" },
                    { text: "나는 다른 사람들에게 나의 좋은 모습만을 보여주려는 경향이 있다.", type: 3, id: "h_3_3" },
                    { text: "나는 경쟁심이 많고 이기고 싶어하는 마음이 강하다.", type: 3, id: "h_3_4" },
                    { text: "다른 사람들이 내가 이룬 일을 인정하지 않을 때 아주 마음이 불편하다.", type: 3, id: "h_3_5" },
                    { text: "나는 목적의식과 정열을 가지고 일을 추진한다.", type: 3, id: "h_3_6" },
                    { text: "일을 효율적으로 처리하고 잘 조직하며 한 번에 여러가지 일을 할 수 있다.", type: 3, id: "h_3_7" },
                    { text: "나는 의미없이 시간을 낭비하는 것을 싫어한다.", type: 3, id: "h_3_8" },
                    { text: "어떤 면에서는 무대체질이 있어서 다른 사람들의 눈에 띄는 것을 좋아한다.", type: 3, id: "h_3_9" },
                    { text: "나는 거의 항상 바쁘다.", type: 3, id: "h_3_10" },

                    { text: "나는 상징(시, 비유, 예술 등)적인 것에 마음이 끌린다.", type: 4, id: "h_4_1" },
                    { text: "제대로 이해받지 못하는 것은 나에게 특히 고통스러운 일이다.", type: 4, id: "h_4_2" },
                    { text: "나는 나의 직관을 소중하게 생각하며 크게 의존한다.", type: 4, id: "h_4_3" },
                    { text: "나는 감정기복이 크고 잘 운다. 아름다움, 사랑, 슬픔과 고통이 쉽게 와 닿는다.", type: 4, id: "h_4_4" },
                    { text: "나는 나에게 결함 또는 결핍된 무엇이 있음을 자주 느낀다.", type: 4, id: "h_4_5" },
                    { text: "나는 삶의 슬픔과 비극적인 면을 가깝게 여긴다.", type: 4, id: "h_4_6" },
                    { text: "때때로 삶은 너무나 평범하고 지루하다.", type: 4, id: "h_4_7" },
                    { text: "나는 다른 사람의 고통을 함께 느낄 때가 많다.", type: 4, id: "h_4_8" },
                    { text: "나는 내가 비극의 주인공처럼 느껴질때가 있다.", type: 4, id: "h_4_9" },
                    { text: "나는 버려졌다고 느낄때가 많다.", type: 4, id: "h_4_10" }
                ],
                head: [ 
                    { text: "문제가 생기면 스스로 해결하는 것이 마음 편해 다른 사람과 의논하지 않는다.", type: 5, id: "hd_5_1" },
                    { text: "시간과 금전에 관해서 낭비하고 싶지 않아서 인색해 질 때가 있다.", type: 5, id: "hd_5_2" },
                    { text: "일상생활에서 나만의 시간과 공간이 있을 때 편안하게 쉴 수 있다.", type: 5, id: "hd_5_3" },
                    { text: "느낌보다는 생각을 표현하는 것이 내게는 더 쉽게 느껴진다.", type: 5, id: "hd_5_4" },
                    { text: "나는 실제 경험보다 관찰이나 책을 통해 더 많이 배운다.", type: 5, id: "hd_5_5" },
                    { text: "어떤 일에 직접 뛰어들기 전에 남들이 하는 것을 관찰하는 경향이 있다.", type: 5, id: "hd_5_6" },
                    { text: "참견 하거나 지나치게 감정적인 사람 특히 화를 잘 내는 공격적인 사람이 싫다.", type: 5, id: "hd_5_7" },
                    { text: "명확한 주제 없이 잡담하는 것을 좋아하지 않는 편이다.", type: 5, id: "hd_5_8" },
                    { text: "너무 오랫동안 사람들과 가까이 있으면 쉽게 피곤해진다.", type: 5, id: "hd_5_9" },
                    { text: "나는 당시에는 감정을 잘 모르다가 혼자 있을때 나의 감정을 알게 된다.", type: 5, id: "hd_5_10" },

                    { text: "나는 가족과 친구들에게 헌신적이고 충실하다.", type: 6, id: "hd_6_1" },
                    { text: "나는 천성적으로 경계심이 많고 의심이 많은 성격이다.", type: 6, id: "hd_6_2" },
                    { text: "사람들을 신뢰하고 싶지만 그들의 동기가 의심스러울 때가 많다. (예:칭찬)", type: 6, id: "hd_6_3" },
                    { text: "분명한 지침과 내가 어디에 서 있는지를 알고 싶어 한다.", type: 6, id: "hd_6_4" },
                    { text: "나는 가장 나쁜 결과를 예측하고 그것에 대해 걱정할 때가 많다.", type: 6, id: "hd_6_5" },
                    { text: "나는 평소엔 불안과 걱정을 많이 느끼지만 위기의 순간엔 문제를 잘 해결해 낸다.", type: 6, id: "hd_6_6" },
                    { text: "규칙을 잘 지키는 편이지만 모순된 규칙은 여지없이 깨뜨려 버린다.", type: 6, id: "hd_6_7" },
                    { text: "책임을 맡는 것이 싫지만 맡은일에는 책임을 다하고 열심히 일한다.", type: 6, id: "hd_6_8" },
                    { text: "나는 지나치게 생각하여 의사결정이 어렵다. 그러나 때로는 돌진하기도 한다.", type: 6, id: "hd_6_9" },
                    { text: "나는 효과가 증명되기 전에는 잘 알려지지 않은 새로운 것을 신뢰하지 않는다.", type: 6, id: "hd_6_10" },
                    
                    { text: "나는 긍정적이고 활달하며 여러 방면에 재능이 있다.", type: 7, id: "hd_7_1" },
                    { text: "여행, 여러가지 음식과 재미있는 일, 모험을 즐길 수 있는 삶을 살고 싶다.", type: 7, id: "hd_7_2" },
                    { text: "나는 어떤 일이 더 이상 재미있게 느껴지지 않을 때 그일을 그만둬 버린다.", type: 7, id: "hd_7_3" },
                    { text: "나는 심각하고 어두운 면을 직면하는 것이 두렵고 어두운 이야기가 싫다.", type: 7, id: "hd_7_4" },
                    { text: "나는 차근차근 실천하는 것 보다 아이디어를 내고 계획하는 것이 더 좋다.", type: 7, id: "hd_7_5" },
                    { text: "고생에서 얻을 수 있는 교훈보다는 즐거움으로 가득 찬 인생을 살고 싶다.", type: 7, id: "hd_7_6" },
                    { text: "나는 다른 사람의 관심을 끌기를 좋아하고 재미있는 이야기나 농담을 즐긴다.", type: 7, id: "hd_7_7" },
                    { text: "내 달력은 계획으로 가득 차 있으며 나는 바쁘게 지내는 것을 좋아한다.", type: 7, id: "hd_7_8" },
                    { text: "때때로 나는 내 멋대로 하고 과도하게 어떤 일에 빠져든다.", type: 7, id: "hd_7_9" },
                    { text: "내 문제 중 하나는 너무 산만하고 집중을 잘 못한다는 것이다.", type: 7, id: "hd_7_10" }
                ],
                gut: [ 
                    { text: "나는 내가 필요로 하는 것을 위해 싸우는 것이 겁나지 않는다.", type: 8, id: "g_8_1" },
                    { text: "힘을 행사하는 일이 통쾌하고 모든 것을 내 통제안에 두고 싶다.", type: 8, id: "g_8_2" },
                    { text: "내가 사람들에게 관심을 갖게 되면 '나의 사람들'이라고 느끼고 보호해준다.", type: 8, id: "g_8_3" },
                    { text: "나는 의지가 강한 사람이며 도전할 수 있는 대상이 있을 때 힘이 솟는다.", type: 8, id: "g_8_4" },
                    { text: "이용당하거나 나를 조롱하는 사람을 가만 두지 않는다.", type: 8, id: "g_8_5" },
                    { text: "타인의 약점을 빨리 알아차리며 나에게 공격해 올 경우에 그 약점을 공격한다.", type: 8, id: "g_8_6" },
                    { text: "사람들과 대결하는 것을 두려워하지 않으며 실제로 자주 대결하는 편이다.", type: 8, id: "g_8_7" },
                    { text: "나는 크게 화를 낼 때가 있다. 그러나 곧 가라앉는다.", type: 8, id: "g_8_8" },
                    { text: "의리와 도리를 중요하게 생각한다.", type: 8, id: "g_8_9" },
                    { text: "나는 단순한 사람이다.", type: 8, id: "g_8_10" },

                    { text: "나는 아주 느긋한 사람이며 무난한 편이다.", type: 9, id: "g_9_1" },
                    { text: "아무 것도 하지 않고 있을 때가 솔직히 가장 좋다.", type: 9, id: "g_9_2" },
                    { text: "다른 사람의 관점이 쉽게 이해되고 내 주장을 내세우기보다 동의할때가 많다.", type: 9, id: "g_9_3" },
                    { text: "마지막 순간까지 일을 미루지만 끝에는 일을 해 낸다.", type: 9, id: "g_9_4" },
                    { text: "모든 선택의 이로운 점, 불리한 점을 다 알고 있기 때문에 결정이 어렵다.", type: 9, id: "g_9_5" },
                    { text: "나는 육체적인 안락함을 중요하게 여기고 잠이 많은 편이다.", type: 9, id: "g_9_6" },
                    { text: "나는 감정에 좌우되지 않는 공평한 중재자이다.", type: 9, id: "g_9_7" },
                    { text: "지위나 명성에 관심이 적고, 그것을 위해 경쟁하고 싶은 마음도 별로 없다.", type: 9, id: "g_9_8" },
                    { text: "친구들은 나와 있을 때 편안하고 평화롭게 느껴진다고 말한다.", type: 9, id: "g_9_9" },
                    { text: "나는 대개의 경우 나에게 모든 관심이 집중되고 튀는 것을 바라지 않는다.", type: 9, id: "g_9_10" },

                    { text: "언행일치를 추구하며 말한것은 꼭 지킨다.", type: 1, id: "g_1_1" },
                    { text: "나 자신이나 다른 사람의 불완전함을 최선을 다해 개선하고 싶은 욕구가 많다.", type: 1, id: "g_1_2" },
                    { text: "나는 완벽해지기 위해서 많은 대가를 치른다고 느낀다.", type: 1, id: "g_1_3" },
                    { text: "나는 비판적이며 어디가 잘못되어 있는지 금방 알 수 있다.", type: 1, id: "g_1_4" },
                    { text: "나는 어떤 대가를 치르든지 양심과 원칙에 따라 행동한다.", type: 1, id: "g_1_5" },
                    { text: "대부분의 사람들은 나를 진지하고 융통성 없는 사람이라고 생각한다.", type: 1, id: "g_1_6" },
                    { text: "나의 원칙과 이상은 더 큰 성취를 위해서 노력하도록 나를 고무한다.", type: 1, id: "g_1_7" },
                    { text: "꼼꼼하고 성실하며 정직 하려고 노력하다보니 소심한 부분이 있다.", type: 1, id: "g_1_8" },
                    { text: "나는 실수하는 것을 아주 싫어하고 실수할까봐 준비를 많이 한다.", type: 1, id: "g_1_9" },
                    { text: "긴장을 풀고 쉬는 것에 죄의식을 느끼며 항상 열심히 노력한다.", type: 1, id: "g_1_10" }
                ]
            }
        };

        let currentStep = 0; 
        const userChoices = {
            center: null, 
            type: null,  
            subtype: null 
        };
        let previousChoices = []; // 이전 단계 선택 저장용
        let centerScores = {}; 
        let typeScores = {};  
        let subtypeScores = {}; 

        const stepIndicatorEl = document.getElementById('step-indicator');
        const stepTitleEl = document.getElementById('step-title');
        const instructionEl = document.getElementById('instruction');
        const optionsAreaEl = document.getElementById('options-area');
        const prevButtonEl = document.getElementById('prev-button');
        const nextButtonEl = document.getElementById('next-button');
        const resultAreaEl = document.getElementById('result-area');
        const resultContentEl = document.getElementById('result-content');
        const restartButtonEl = document.getElementById('restart-button');
        const errorMessageEl = document.getElementById('error-message');
        const questionTitleAreaEl = document.getElementById('question-title-area');

        function renderStep() {
            optionsAreaEl.innerHTML = ''; 
            errorMessageEl.classList.add('hidden');
            stepIndicatorEl.textContent = `진행 단계: ${currentStep + 1} / 4`;
            prevButtonEl.classList.toggle('hidden', currentStep === 0); // 첫 단계에서는 이전 버튼 숨김

            if (currentStep === 0) { 
                stepTitleEl.textContent = "1단계: 나의 주요 경향성 찾기";
                instructionEl.textContent = "다음 각 그룹의 질문들에 대해 자신에게 해당하는 정도를 선택해주세요. (1점: 전혀 아니다 ~ 5점: 매우 그렇다)";
                enneagramData.centerIdentificationGroups.forEach(group => {
                    const groupDiv = document.createElement('div');
                    groupDiv.classList.add('question-group');
                    const groupTitle = document.createElement('h3');
                    groupTitle.textContent = group.groupName;
                    groupDiv.appendChild(groupTitle);
                    group.questions.forEach(q => {
                        groupDiv.appendChild(createRatingQuestionElement(q.text, q.id, `q_center_${q.id}`));
                    });
                    optionsAreaEl.appendChild(groupDiv);
                });
                nextButtonEl.textContent = "다음 🚀";
            } else if (currentStep === 1) { 
                stepTitleEl.textContent = `2단계: 기본 유형 찾기`; 
                instructionEl.textContent = "다음 질문들에 대해 자신에게 해당하는 정도를 선택해주세요. (1점: 전혀 아니다 ~ 5점: 매우 그렇다)";
                const questions = enneagramData.centerQuestions[userChoices.center.id]; 
                questions.forEach(q => {
                    optionsAreaEl.appendChild(createRatingQuestionElement(q.text, q.id, `q_type_${q.id}`));
                });
                nextButtonEl.textContent = "다음 🚀";
            } else if (currentStep === 2) { 
                stepTitleEl.textContent = `3단계: 하위 경향성 찾기`; // 익명화된 제목
                instructionEl.textContent = "다음 각 그룹의 질문들에 대해 자신에게 해당하는 정도를 선택해주세요. (1점: 전혀 아니다 ~ 5점: 매우 그렇다)";
                const selectedTypeData = enneagramData.types[userChoices.type.id];
                
                // 하위 유형 그룹 제목 익명화 (X, Y, Z)
                const subtypeGroupNames = ["X 그룹 질문", "Y 그룹 질문", "Z 그룹 질문"];
                let groupIndex = 0;

                for (const subtypeKey in selectedTypeData.subtypes) {
                    const subtypeInfo = selectedTypeData.subtypes[subtypeKey];
                    const groupDiv = document.createElement('div');
                    groupDiv.classList.add('question-group');
                    const groupTitle = document.createElement('h3');
                    groupTitle.textContent = subtypeGroupNames[groupIndex % subtypeGroupNames.length]; 
                    groupIndex++;
                    groupDiv.appendChild(groupTitle);
                    
                    subtypeInfo.questions.forEach(q => {
                        groupDiv.appendChild(createRatingQuestionElement(q.text, q.id, `q_subtype_${q.id}`));
                    });
                    optionsAreaEl.appendChild(groupDiv);
                }
                nextButtonEl.textContent = "결과 보기 🌟";
            } else if (currentStep === 3) { 
                displayResult();
                prevButtonEl.classList.add('hidden'); // 결과 화면에서는 이전 버튼 숨김
                nextButtonEl.classList.add('hidden'); // 결과 화면에서는 다음 버튼 숨김
            }
            // 이전 단계의 선택 복원
            if (previousChoices[currentStep]) {
                previousChoices[currentStep].forEach(choice => {
                    const radio = document.querySelector(`input[name="${choice.name}"][value="${choice.value}"]`);
                    if (radio) radio.checked = true;
                });
            }
        }
        
        function createRatingQuestionElement(questionText, questionBaseId, nameAttribute) {
            const questionDiv = document.createElement('div');
            questionDiv.classList.add('question-item');
            const uniqueName = nameAttribute.startsWith('q_center_') ? `q_center_${questionBaseId}` :
                                nameAttribute.startsWith('q_type_') ? `q_type_${questionBaseId}` :
                                `q_subtype_${questionBaseId}`;

            questionDiv.innerHTML = `
                <p class="mb-3 text-gray-700">${questionText}</p>
                <div class="rating-options space-x-1 flex flex-wrap justify-center md:justify-start">
                    ${[1,2,3,4,5].map(val => `
                        <input type="radio" id="${uniqueName}_${val}" name="${uniqueName}" value="${val}" class="sr-only">
                        <label for="${uniqueName}_${val}">${val}점</label>
                    `).join('')}
                </div>
            `;
            return questionDiv;
        }
        
        function displayResult() {
            questionTitleAreaEl.classList.add('hidden');
            optionsAreaEl.classList.add('hidden');
            nextButtonEl.classList.add('hidden');
            prevButtonEl.classList.add('hidden');
            stepIndicatorEl.classList.add('hidden');
            resultAreaEl.classList.remove('hidden');

            resultContentEl.innerHTML = `
                <div class="result-section bg-blue-50">
                    <h3 class="text-blue-700">💖 중심 에너지: ${userChoices.center.name}</h3>
                    <p>${userChoices.center.description}</p>
                </div>
                <div class="result-section bg-green-50">
                    <h3 class="text-green-700">✨ 기본 유형: ${userChoices.type.name}</h3>
                    <p>${userChoices.type.description}</p>
                </div>
                <div class="result-section bg-yellow-50">
                    <h3 class="text-yellow-700">🌟 하위 유형: ${userChoices.subtype.name}</h3>
                    <p>${userChoices.subtype.description}</p>
                </div>
                <hr class="my-6 border-pink-200">
                <p class="text-sm text-gray-600">이 테스트는 자기 이해를 돕기 위한 참고 자료이며, 전문적인 진단을 대체할 수 없습니다. 에니어그램은 개인의 성장과 발달을 위한 도구로 활용될 때 더욱 의미가 있습니다. 각 유형의 더 자세한 특징, 건강/불건강 상태, 날개 유형, 발달 방향 등은 추가적인 학습을 통해 알아보시는 것을 권장합니다.</p>
            `;
        }
        
        function saveCurrentChoices() {
            const currentRadios = optionsAreaEl.querySelectorAll('input[type="radio"]:checked');
            const choicesToSave = [];
            currentRadios.forEach(radio => {
                choicesToSave.push({ name: radio.name, value: radio.value });
            });
            previousChoices[currentStep] = choicesToSave;
        }

        prevButtonEl.addEventListener('click', () => {
            if (currentStep > 0) {
                currentStep--;
                // 이전 단계로 갈 때, 현재 단계 이후의 선택은 초기화
                if (currentStep === 0) { // 1단계로 돌아가면 모든 선택 초기화
                    userChoices.center = null;
                    userChoices.type = null;
                    userChoices.subtype = null;
                    centerScores = {};
                    typeScores = {};
                    subtypeScores = {};
                    previousChoices = []; // 모든 저장된 선택 초기화
                } else if (currentStep === 1) { // 2단계로 돌아가면 type, subtype 초기화
                    userChoices.type = null;
                    userChoices.subtype = null;
                    typeScores = {};
                    subtypeScores = {};
                    previousChoices.splice(2); // 3단계, 4단계 선택 기록 삭제
                } else if (currentStep === 2) { // 3단계로 돌아가면 subtype 초기화
                    userChoices.subtype = null;
                    subtypeScores = {};
                    previousChoices.splice(3); // 4단계 선택 기록 삭제
                }
                renderStep();
                optionsAreaEl.scrollTop = 0;
            }
        });


        nextButtonEl.addEventListener('click', () => {
            errorMessageEl.classList.add('hidden'); 
            saveCurrentChoices(); // 다음으로 넘어가기 전 현재 선택 저장
            
            let allAnsweredInStep = true; 

            if (currentStep === 0) { 
                centerScores = { heart: 0, head: 0, gut: 0 }; 
                enneagramData.centerIdentificationGroups.forEach(group => {
                    group.questions.forEach(q => {
                        const selectedRating = document.querySelector(`input[name="q_center_${q.id}"]:checked`);
                        if (selectedRating) {
                            centerScores[q.centerTarget] += parseInt(selectedRating.value);
                        } else {
                            allAnsweredInStep = false;
                        }
                    });
                });

                if (!allAnsweredInStep) {
                    errorMessageEl.textContent = "모든 그룹의 질문에 답변해주세요.";
                    errorMessageEl.classList.remove('hidden');
                    return;
                }

                let maxCenterScore = -1;
                let dominantCenterId = null;
                const centerOrder = ["heart", "head", "gut"];
                for (const centerId of centerOrder) {
                    if (centerScores[centerId] > maxCenterScore) {
                        maxCenterScore = centerScores[centerId];
                        dominantCenterId = centerId;
                    } else if (centerScores[centerId] === maxCenterScore) { 
                        if (dominantCenterId === null || (centerOrder.indexOf(centerId) < centerOrder.indexOf(dominantCenterId))) {
                            dominantCenterId = centerId;
                        }
                    }
                }
                if (dominantCenterId === null) dominantCenterId = "heart"; 

                const centerData = enneagramData.centers.find(c => c.id === dominantCenterId);
                userChoices.center = { id: centerData.id, name: centerData.name, description: centerData.description };

            } else if (currentStep === 1) { 
                const questions = enneagramData.centerQuestions[userChoices.center.id];
                typeScores = {}; 
                
                questions.forEach(q => {
                    const selectedRating = document.querySelector(`input[name="q_type_${q.id}"]:checked`);
                    if (selectedRating) {
                        const score = parseInt(selectedRating.value);
                        typeScores[q.type] = (typeScores[q.type] || 0) + score;
                    } else {
                        allAnsweredInStep = false;
                    }
                });

                if (!allAnsweredInStep) {
                    errorMessageEl.textContent = "모든 기본 유형 질문에 답변해주세요.";
                    errorMessageEl.classList.remove('hidden');
                    return;
                }

                let maxTypeScore = -1;
                let dominantType = null;
                const centerTypeIds = enneagramData.centers.find(c => c.id === userChoices.center.id).types;
                
                for (const typeId of centerTypeIds) { 
                    if (typeScores[typeId] !== undefined && typeScores[typeId] > maxTypeScore) {
                        maxTypeScore = typeScores[typeId];
                        dominantType = typeId;
                    } else if (typeScores[typeId] !== undefined && typeScores[typeId] === maxTypeScore) {
                        if (dominantType === null || (centerTypeIds.indexOf(typeId) < centerTypeIds.indexOf(dominantType))) {
                            dominantType = typeId;
                        }
                    }
                }
                                
                if (dominantType === null && centerTypeIds.length > 0) { 
                    dominantType = centerTypeIds[0];
                }

                const typeData = enneagramData.types[dominantType];
                userChoices.type = { id: dominantType, name: typeData.name, description: typeData.description };

            } else if (currentStep === 2) { 
                subtypeScores = { sp: 0, sx: 0, so: 0 };
                const selectedTypeData = enneagramData.types[userChoices.type.id];

                for (const subtypeKey in selectedTypeData.subtypes) {
                    selectedTypeData.subtypes[subtypeKey].questions.forEach(q => {
                        const selectedRating = document.querySelector(`input[name="q_subtype_${q.id}"]:checked`);
                        if (selectedRating) {
                            subtypeScores[subtypeKey] += parseInt(selectedRating.value);
                        } else {
                            allAnsweredInStep = false;
                        }
                    });
                }
                
                if (!allAnsweredInStep) {
                    errorMessageEl.textContent = "모든 하위 유형 질문에 답변해주세요.";
                    errorMessageEl.classList.remove('hidden');
                    return;
                }

                let maxSubtypeScore = -1;
                let dominantSubtypeKey = null;
                const subtypeOrder = ["sp", "sx", "so"]; 
                for (const subKey of subtypeOrder) {
                    if (subtypeScores[subKey] > maxSubtypeScore) {
                        maxSubtypeScore = subtypeScores[subKey];
                        dominantSubtypeKey = subKey;
                    } else if (subtypeScores[subKey] === maxSubtypeScore) {
                        if (dominantSubtypeKey === null || (subtypeOrder.indexOf(subKey) < subtypeOrder.indexOf(dominantSubtypeKey))) {
                            dominantSubtypeKey = subKey;
                        }
                    }
                }
                if (dominantSubtypeKey === null) dominantSubtypeKey = "sp"; 

                const subtypeData = selectedTypeData.subtypes[dominantSubtypeKey];
                userChoices.subtype = { id: dominantSubtypeKey, name: subtypeData.name, description: subtypeData.description };
            }
            
            currentStep++;
            if (currentStep < 3) { 
                document.getElementById('options-area').scrollTop = 0;
            }
            renderStep();
        });

        restartButtonEl.addEventListener('click', () => {
            currentStep = 0;
            userChoices.center = null;
            userChoices.type = null;
            userChoices.subtype = null;
            centerScores = {};
            typeScores = {};
            subtypeScores = {};
            previousChoices = [];
            
            questionTitleAreaEl.classList.remove('hidden');
            optionsAreaEl.classList.remove('hidden');
            nextButtonEl.classList.remove('hidden');
            prevButtonEl.classList.remove('hidden');
            resultAreaEl.classList.add('hidden');
            errorMessageEl.classList.add('hidden');
            stepIndicatorEl.classList.remove('hidden');
            document.getElementById('options-area').scrollTop = 0;
            renderStep();
        });

        renderStep();
    </script>
</body>
</html>
"""

# Streamlit 컴포넌트를 사용하여 HTML 렌더링
# height는 HTML 내용이 충분히 보일 수 있도록 적절히 조절해주세요.
# 일반적으로 JavaScript를 포함한 동적 컨텐츠는 높이를 예측하기 어려우므로,
# 충분한 값을 주거나, scrolling=True 옵션을 고려할 수 있습니다.
components.html(html_code, height=800, scrolling=True)

# 또는 st.markdown을 사용할 수도 있습니다.
# st.markdown(html_code, unsafe_allow_html=True)
