import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    html = """
        <div style='margin: auto; width: 50vw; text-align: center;'>
            <h1> Main page </h1>
            <div style='margin-top: 10vh'>
                <h3>
                    Welcome to the website written in Django.
                </h3>
            </div>
            <div>
                <a href='/about/'>About me</a>
            </div>
        </div>
         """
    logger.info('Visited main page.')
    return HttpResponse(html)


def about(request):
    html = """
        <div style='margin: auto; width: 50vw;'>
            <h1 style='text-align: center;'> About me </h1>
            <div style=''>
                <h3>
                    First name: Elena
                </h3>
            </div>
            <div style=''>
                <h3>
                    Last name: Savostyanova
                </h3>
            </div>
            <div style=''>
                <h3>
                    About me:
                </h3>
            </div>
            <div>
                <h5>
                <p>
                Я студент платформы GeekBrains. Сейчас я активно изучаю стек
                технологий, включающий в себя Django, REST DRF, PostgreSQL,
                Jinja, а также языки программирования Python, C# и Java. Хочу
                поделиться с вами своим опытом и впечатлениями о том, как
                проходит мой путь к освоению всех этих инструментов.
                </p>
                <p>
                Одной из ключевых технологий, которую я изучаю,
                является Django. Этот фреймворк для веб-разработки на Python
                предоставляет множество инструментов для создания мощных и
                масштабируемых веб-приложений. REST DRF, в свою очередь,
                позволяет создавать API на основе архитектурных принципов REST,
                что делает взаимодействие между клиентом и сервером
                эффективным и удобным.
                </p>
                </h5>
            </div>
            <div>
                <a href='/'>To main page</a>
            </div>
        </div>

    """
    logger.info('Visited page about me.')
    return HttpResponse(html)
