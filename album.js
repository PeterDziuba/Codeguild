"use strict";

function getURL() {
  return $('#pictureURL').val();
}

function getImageFromURL(url) {
  var imageFromURL = $("<img></img>").attr("src", url).attr("width", 300).attr("height", 300);
  return imageFromURL;
}

function putImageInArticle(image) {
  var articleWithImage = $("<article></article>").attr("width", 300).attr("class", "big-article");
  return articleWithImage.append(image);
}

function putURLIntoArticle(url) {
  var linkToURL = $("<a>Link to this image</a>").attr("href", url);
  var articleBox = $("<article></article>").attr("class", "article-with-button-and-link");
  articleBox = articleBox.append(linkToURL);
  articleBox = articleBox.append("<br>");
  return articleBox;
}

function createButton(articleWithImageAndLink) {
  var ourButton = $("<button>").text("Delete").attr("href", "");
  ourButton.on("click", function (event) {
    event.preventDefault();
    articleWithImageAndLink.remove();
    updateHeader();
  });
  return ourButton;
}

function updateHeader() {
  $("h1").text($("img").length);
}

function putButtonIntoArticle(articleBox, button) {
  var articleWithImageAndLinkAndButton = articleBox.append(button);
  return articleWithImageAndLinkAndButton;
}

function putArticleInDiv(articleWithImageAndLinkAndButton) {
  $("div").append(articleWithImageAndLinkAndButton);
}

function getSubmission() {
  var ourURL = getURL();
  var ourImage = getImageFromURL(ourURL);
  var articleWithImage = putImageInArticle(ourImage);
  var articleBox = putURLIntoArticle(ourURL);
  var ourButton = createButton(articleWithImage);
  var articleWithLinkAndButton = putButtonIntoArticle(articleBox, ourButton);
  var articleWithImageAndLinkAndButton = articleWithImage.append(articleWithLinkAndButton);
  putArticleInDiv(articleWithImageAndLinkAndButton);
}

function registerEverything() {
  $("form").on("submit", function(event) {
    event.preventDefault();
    getSubmission();
    updateHeader();
  })
}


$(document).ready( function() {
  registerEverything();
});