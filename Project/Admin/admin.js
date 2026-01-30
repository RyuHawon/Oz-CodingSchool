const product_data = [
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
];

const productTableBody = document.getElementById('product_data_Table');
const searchForm = document.getElementById('searchForm');

function renderTable(items) {
    productTableBody.innerHTML = '';
    items.forEach((item) => {
        const row = productTableBody.insertRow();
        row.insertCell(0).innerHTML = item.category;
        row.insertCell(1).innerHTML = item.brand;
        row.insertCell(2).innerHTML = item.product;
        row.insertCell(3).innerHTML = item.price;
    });
}

searchForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const categoryVal = document.getElementById('inlineFormSelectPeref').value;
    const searchVal = document.getElementById('searched_name').value.toLowerCase();

    const filtered = product_data.filter(item => {
        const isCategoryMatch = (categoryVal === 'all' || item.category === categoryVal);
        const isNameMatch = item.product.toLowerCase().includes(searchVal);
        return isCategoryMatch && isNameMatch;
    });

    renderTable(filtered);
});

function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-bs-theme');
    const newTheme = (currentTheme === 'dark') ? 'light' : 'dark';
    html.setAttribute('data-bs-theme', newTheme);
}

renderTable(product_data);