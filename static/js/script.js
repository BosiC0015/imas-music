// global
const brandName = {
  "as": "THE IDOLM@STER",
  "cg": "Cinderella Girls",
  "ml": "Million Live",
  "m": "Side M",
  "sc": "Shiny Colors",
  "gkms": "Gakuen IDOLM@STER",
  "others": "Others"
}

const brandIconsSrc = {
  "as": "/static/images/765as.svg",
  "cg": "/static/images/cg.svg",
  "ml": "/static/images/ml.svg",
  "m": "/static/images/m.svg",
  "sc": "/static/images/sc.svg",
  "gkms": "/static/images/gkms.svg",
  "others": "/static/images/others.svg"
};

// get brand icon
const getBrandIconSrc = (brand) => {
  return brandIconsSrc[brand];
};


// nav expand and collapse
const navExpandButton = document.getElementById('nav-expand-button');
const navCollapseButton = document.getElementById('nav-collapse-button')
const navCollapsed = document.getElementById('nav-collapsed');
const navExpanded = document.getElementById('nav-expanded');

const navExpand = () => {
  navExpanded.classList.remove('hide');
  navCollapsed.classList.add('hide');
  navCollapseButton.classList.remove('hide');
  navExpandButton.classList.add('hide');
};

const navCollapse = () => {
  navExpanded.classList.add('hide');
  navCollapsed.classList.remove('hide');
  navCollapseButton.classList.add('hide');
  navExpandButton.classList.remove('hide');
};

navExpandButton.addEventListener('click', function() {
  navExpand();
});

navCollapseButton.addEventListener('click', function() {
  navCollapse();
});


// search bar



//container for latest 5 releases
const latestReleaseContainer = document.getElementById('latest-releases');

const createCover = (cover, title) => {
  const articleImg = document.createElement('div');
  articleImg.classList.add('article-img');
  
  const coverImg = document.createElement('img');
  coverImg.src = cover;
  coverImg.alt = title;
  coverImg.style = "width: 200px;";
  
  articleImg.append(coverImg);
  return articleImg
}

const createListItem = (content) => {
  const item = document.createElement('li');
  item.textContent = content;
  return item;
}

const createTrackList = (tracksArr) => {
  const list = document.createElement('ol');
  tracksArr.forEach(t => list.append(createListItem(t)));
  return list;
}

const createInfoCard = (title, tracksArr) => {
  const infoCard = document.createElement('div');
  infoCard.classList.add('article-info');
  
  const releaseTitle = document.createElement('h3');
  releaseTitle.textContent = title;
  infoCard.append(releaseTitle);

  const trackList = createTrackList(tracksArr);
  infoCard.append(trackList);
  
  return infoCard;
}

const createBrandIcon = (brand) => {
  const articleBrand = document.createElement('div');
  articleBrand.classList.add('article-brand');
  
  const icon = document.createElement('img');
  icon.src = getBrandIconSrc(brand);
  icon.alt = `${brandName[brand]} icon`;
  icon.style = "width: 50px;";
  
  articleBrand.append(icon);
  return articleBrand
}

const createArticle = (data) => {
  // data was in object form
  // const brand = data["series_test"]["brand"];
  // const cover = data["cover_img"];
  // const title = data["title"];
  // const tracksArr = data["track_list"];

  // but now in array...
  const brand = data[11];
  const cover = data[3];
  const title = data[1];
  const tracksArr = data[8];

  const article = document.createElement('article');
  article.classList.add(`${brand}-shadow`);

  article.append(createCover(cover, title));
  article.append(createInfoCard(title, tracksArr));
  article.append(createBrandIcon(brand));

  return article;
}

const createReleaseCard = (brand, title) => {
  const card = document.createElement('div');
  releaseTitle.textContent = title;
  card.append(createIcon(brand));
  card.append(title);
}

// console.log(appData) // for debugging
appData.forEach(e => latestReleaseContainer.append(createArticle(e))); 