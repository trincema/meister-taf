class LoginTest extends GroovyTestCase {

    @Test
    public void testLength() {
        def result = length([2, 3, 8, 9, 0, 1, 5, 7])
        assert result == 8
    }

}