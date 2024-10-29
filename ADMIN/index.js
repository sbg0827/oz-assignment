// const form = document.getElementById("form")

// form.addEventListener("submit", function(event){
//     event.preventDefault() // 기존 기능 차단

//     let userId =event.target.id.value
//     let userPw1 = event.target.pw1.value
//     let userPw2 = event.target.pw2.value
//     let userName = event.target.name.value
//     let userPhone = event.target.phone.value
//     let userGender = event.target.gender.value
//     let userEmail = event.target.email.value

//     if(userId. length < 6){
//         alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요")
//         return
//     }

//     if(userPw1 !== userPw2){
//         alert("비밀번호가 일치하지 않습니다.")
//         return
//     }

//     alert(
//         `${userId}님 환영합니다
//         회원가입 시 입력하신 내역은 다음과 같습니다
//         아이디 : ${userid}
//         전화번호 : ${userphone}
//     `)});

const form = document.getElementById("form")

form.addEventListener("submit", function(event){
    event.preventDefault() // 기존 기능 차단

    let userId =event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value

    if(userId. length < 6){
        alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요")
        return
    }

    if(userPw1. length < 8){
        alert("비밀번호가 너무 짧습니다. 8자 이상 입력해주세요")
        return
    }

    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    alert(
        `${userId}님 환영합니다
        회원가입 시 입력하신 내역은 다음과 같습니다
        아이디 : ${userId}
        비밀번호 : ${userPw1}
        이름 : ${userName}
        전화번호 : ${userPhone}
        성별 : ${userGender}
        이메일 : ${userEmail}`)

        document.body.innerHTML = "2day.html"
        document.write(`<p>${userId}님 환영합니다
            </p>`)
})

    