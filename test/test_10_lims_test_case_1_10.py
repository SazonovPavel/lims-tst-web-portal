# Login and logout  для физ лица

def test_10_lims_test_case_1_10(app):
    app.session.login(password='111', path_to_key='C:/87654321_87654321_DU180904160002.ZS2')
    app.session.logout()
