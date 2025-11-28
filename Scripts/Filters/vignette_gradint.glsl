uniform sampler2D bgl_RenderedTexture;
uniform vec2 bgl_RenderedTextureSize;

void main()
{
    vec2 uv = gl_TexCoord[0].st;

    vec4 color = texture2D(bgl_RenderedTexture, uv);

    // Centro da tela (normalizado)
    vec2 center = vec2(0.5, 0.5);

    // Distância radial do pixel ao centro (0.0 no meio, 1.0 nas bordas)
    float dist = distance(uv, center);

    // Controle da força da vinheta
    float strength = 1.3; // aumenta para escurecer mais
    float vignette = smoothstep(0.1, strength, dist); // onde começa e termina o escurecimento

    // Aplica a vinheta (multiplica por preto)
    color.rgb *= 1.0 - vignette;

    gl_FragColor = color;
}
