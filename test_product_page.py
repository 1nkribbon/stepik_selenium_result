from .pages.product_page import ProductPage


def test_guest_can_add_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_basket_btn()
