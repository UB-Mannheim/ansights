import sys
import os
sys.path.append('./')
sys.path.append('./../')
sys.path.append('./../..')
if True:
    from src.utils.__RepoPath__ import repo_path
    from src.utils.logger import get_logger
    from tesseract import get_string
    from fuse_keywords import fuse
    from lobid_api import get_gnd_keywordRelations
logger = get_logger('MAIN')

TEST_PATH = os.path.join(repo_path, 'data/2013_0473_023__ansicht01.tif')


def main():
    ocr_text = get_string(TEST_PATH, lang='deu_frak')
    logger.info('OCR returned text: %s' % ocr_text)
    keywords_with_score = fuse(ocr_text, max_nouns=5, max_verbs=3)
    keywords = list(keywords_with_score.keys())
    logger.info(f'Extracted Keywords: {keywords}')
    keywords_extended = dict(get_gnd_keywordRelations(keywords=keywords, max_query_items=30, print_output=False, verbose=False,
                                                      max_keyword_relations=3))
    logger.info(f'GND-Extended Keywords: {keywords_extended}')


if __name__ == '__main__':
    logger.info('==== Starting Main Program =====')
    main()