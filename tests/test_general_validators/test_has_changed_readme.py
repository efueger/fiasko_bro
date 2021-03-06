from fiasko_bro import validators


def test_readme_changed_succeeds(test_repo, origin_repo):
    output = validators.has_changed_readme(
        solution_repo=test_repo,
        readme_filename='changed_readme.md',
        original_repo=origin_repo,
    )
    assert output is None


def test_readme_changed_fails(test_repo, origin_repo):
    expected_output = 'need_readme', None
    output = validators.has_changed_readme(
        solution_repo=test_repo,
        readme_filename='unchanged_readme.md',
        original_repo=origin_repo,
    )
    assert output == expected_output
