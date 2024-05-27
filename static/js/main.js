let originalText = "";
let replacements = new Map(); // Thêm biến này để lưu trữ các thay thế

$(document).ready(function () {
    $('#checkBtn').click(() => {
        const text = $("#textToCheck").val();
        originalText = text;
        replacements.clear(); // Xóa các thay thế trước đó
        if (text) {
            $.ajax({
                type: "POST",
                url: `/`,
                contentType: 'application/json',
                data: JSON.stringify({ text }),
                success: (result) => {
                    const listWrong = $("#listWrongText");
                    listWrong.html("");
                    result.forEach((ele) => {
                        listWrong.append(
                            `<a href='javascript:void(0)' class='list-group-item list-group-item-action'
                               data-text='${JSON.stringify(ele.suggest)}' 
                               data-wrong='${ele.wrong}'
                               onclick='setRecommentText(this)'>
                                ${ele.wrong}
                            </a>`
                        );
                    });
                },
                error: (xhr, status, error) => {
                    console.error("Error: ", status, error);
                    alert("An error occurred. Please try again.");
                }
            });
        } else {
            alert("Please enter text");
        }
    });
});

function setRecommentText(ele) {
    const suggestions = JSON.parse($(ele).attr('data-text'));
    const wrongText = $(ele).attr('data-wrong');
    const listRecomment = $("#listRecommentText");
    listRecomment.html("");
    suggestions.forEach((suggestion) => {
        listRecomment.append(
            `<a href='javascript:void(0)' class='list-group-item list-group-item-action'
               onclick='selectReplacement("${wrongText}", "${suggestion}")'>
                ${suggestion}
            </a>`
        );
    });
}

function selectReplacement(wrongText, suggestion) {
    replacements.set(wrongText, suggestion); // Lưu thay thế vào map
    updateText(); // Cập nhật văn bản với tất cả các thay thế đã chọn
}

function updateText() {
    let updatedText = originalText;
    replacements.forEach((value, key) => {
        updatedText = updatedText.replace(new RegExp(`\\b${key}\\b`, 'g'), value);
    });
    $("#updatedText").text(updatedText); // Cập nhật văn bản đã sửa
}
