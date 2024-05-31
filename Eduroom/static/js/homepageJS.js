let profileDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");

let classList = profileDropdownList.classList;

const toggle = () => classList.toggle("active");

window.addEventListener("click", function (e) {
  if (!btn.contains(e.target)) classList.remove("active");
});

const result = document.querySelector('.result');

let keywords = [
  "coffeshop",
  "drug store",
  "toilet",
];

let list = [];

const highlightMatch = (value, inputKeyword) => {
  const regex = new RegExp(`(${inputKeyword})`, 'gi');
  return value.replace(regex, '<strong>$1</strong>');
};

const liTag = (value) => {
  return `<li><i class="fa-solid fa-magnifying-glass"></i><a href="#">${value}</a></li>`;
};

const generateList = () => {
  list = list.map((data) => liTag(data));
  console.log(list);
};

const startsWith = (keyword, inputKeyword) =>
  keyword.toLowerCase().startsWith(inputKeyword.toLowerCase());

const includes = (keyword, inputKeyword) =>
  keyword.toLowerCase().includes(inputKeyword.toLowerCase());

const filter = (inputKeyword) => {
  list = keywords.filter(
    (keyword) => startsWith(keyword, inputKeyword) || includes(keyword, inputKeyword)
  );
};

const showList = (inputKeyword) => {
  result.classList.add('show');
  result.innerHTML = list.join('') || liTag(inputKeyword);
};

const hideList = () => {
  list = [];
  result.innerHTML = list;
  result.classList.remove('show');
};

const search = (e) => {
  let keyword = e.target.value;
  if (keyword) {
    filter(keyword);
    generateList();
    showList(keyword);
  } else hideList();
};

// Event listener untuk input search
const searchInput = document.querySelector('.search input');
searchInput.addEventListener('input', search);


document.addEventListener('DOMContentLoaded', () => {
  const iconLinks = document.querySelectorAll('.icon-links a i');

  iconLinks.forEach(icon => {
    icon.addEventListener('click', (event) => {
      event.preventDefault();
      const link = event.target.parentElement.getAttribute('data-link');
      if (link) {
        navigator.clipboard.writeText(link).then(() => {
          alert('Link copied to clipboard: ' + link);
        }).catch(err => {
          console.error('Failed to copy link: ', err);
        });
      }
    });
  });
});
