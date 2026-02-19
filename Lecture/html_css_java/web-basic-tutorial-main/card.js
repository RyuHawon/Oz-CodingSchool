console.log("Hello World")

// 변수
// const username = "후츠릿";
// let username = "후츠릿";

// const(상수) vs let (변수)

// 이름 바꾸기 로직

// 1. .button 태그 가져오기
const buttonEl = document.querySelector(".button");
console.log("buttonEl", buttonEl);

// 2. 버튼 태그 클릭시 프롬프트 띄우기
// def handleClick():
//     print("어쩌구")

// 3. 사용자 입력받아와서 username 변수에 저장
// 4. .name 태그 가져오기
const nameEl = document.querySelector(".name");
console.dir(nameEl);

const handleClick = () => {
    console.log("click");
    const username = window.prompt("이름을 입력해주세요");
    console.log("🚀 ~ handleClick ~ username:", username);

    // 5. .name 태그의 컨텐츠를 username 값으로 변경
    nameEl.innerText = username
} //화살표 함수

buttonEl.addEventListener("click", handleClick);